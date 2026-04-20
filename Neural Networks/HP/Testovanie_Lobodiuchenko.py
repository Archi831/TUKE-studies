import os
import json
import time
import copy
import random
from pathlib import Path
from typing import Any, Dict, List, Callable, Tuple

import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

import torch
import torch.nn as nn
import torch.optim as optim
import torchvision

from torchvision import transforms
from torch.utils.data import DataLoader, random_split, ConcatDataset

from sklearn.linear_model import LogisticRegression
from sklearn.metrics import (
accuracy_score,
confusion_matrix,
classification_report,
ConfusionMatrixDisplay,
)



# --- Transform ---
transform = transforms.Compose(
    [
        transforms.ToTensor(),
        transforms.Lambda(lambda x: x.view(-1)),
    ]
)

# --- Load MNIST ---
mnist_train_full = torchvision.datasets.MNIST(root="./data", train=True, download=True, transform=transform)
mnist_test = torchvision.datasets.MNIST(root="./data", train=False, download=True, transform=transform)

# --- Split train into train/val ---
generator = torch.Generator().manual_seed(42)
mnist_train, mnist_val = random_split(mnist_train_full, [50000, 10000], generator=generator)

# --- Create DataLoaders ---
_pin = torch.cuda.is_available()
train_loader = DataLoader(mnist_train, batch_size=128, shuffle=True,  pin_memory=_pin, num_workers=0)
val_loader   = DataLoader(mnist_val,   batch_size=128, shuffle=False, pin_memory=_pin, num_workers=0)
test_loader  = DataLoader(mnist_test,  batch_size=128, shuffle=False, pin_memory=_pin, num_workers=0)

# --- Prepare numpy arrays for sklearn ---
def loader_to_numpy(loader):
    X, y = [], []
    for images, labels in loader:
        X.append(images.numpy())
        y.append(labels.numpy())
    return np.vstack(X), np.hstack(y)

X_train, y_train = loader_to_numpy(train_loader)
X_val, y_val = loader_to_numpy(val_loader)
X_test, y_test = loader_to_numpy(test_loader)

print(f"Train shape: {X_train.shape}, {y_train.shape}")

# Class distribution
class_counts = np.bincount(y_train)
plt.figure(figsize=(10, 6))
plt.bar(range(10), class_counts)
plt.xlabel('Class')
plt.ylabel('Count')
plt.title('Class Distribution')
plt.savefig('eda_class_dist.png')
plt.close()

# 5x5 sample grid
fig, axes = plt.subplots(5, 5, figsize=(10, 10))
for i in range(25):
    ax = axes[i // 5, i % 5]
    class_idx = i % 10
    class_samples = np.where(y_train == class_idx)[0]
    sample_idx = class_samples[0]
    ax.imshow(X_train[sample_idx].reshape(28, 28), cmap='gray')
    ax.set_title(f'Class {class_idx}')
    ax.axis('off')
plt.tight_layout()
plt.savefig('eda_samples.png')
plt.close()

# Pixel intensity histogram
plt.figure(figsize=(10, 6))
plt.hist(X_train.flatten(), bins=50, edgecolor='black')
plt.xlabel('Pixel Intensity')
plt.ylabel('Frequency')
plt.title('Pixel Intensity Distribution')
plt.savefig('eda_pixel_hist.png')
plt.close()

# Statistics
print(f"Mean: {X_train.mean():.4f}")
print(f"Std: {X_train.std():.4f}")
print(f"Min: {X_train.min():.4f}")
print(f"Max: {X_train.max():.4f}")

log_reg = LogisticRegression(max_iter=1000, random_state=42)
log_reg.fit(X_train, y_train)
y_pred = log_reg.predict(X_test)
y_val_pred = log_reg.predict(X_val)

cm = confusion_matrix(y_test, y_pred)
plt.figure(figsize=(10, 8))
sns.heatmap(cm, annot=True, fmt='d', cmap='Blues')
plt.xlabel('Predicted')
plt.ylabel('True')
plt.title('Confusion Matrix')
plt.savefig('confusion_matrix.png')
plt.close()

test_acc = accuracy_score(y_test, y_pred)
print(f"Test Accuracy: {test_acc:.4f}")
val_acc = accuracy_score(y_val, y_val_pred)
print(f"Validation Accuracy: {val_acc:.4f}")

def set_seed(seed: int):
    random.seed(seed)
    np.random.seed(seed)
    torch.manual_seed(seed)
    torch.cuda.manual_seed_all(seed)
    torch.backends.cudnn.deterministic = True
    torch.backends.cudnn.benchmark = False

if not torch.cuda.is_available():
    raise RuntimeError("CUDA GPU not available. This notebook requires a GPU.")

DEVICE = torch.device("cuda")
torch.cuda.set_device(0)
print(f"Using device: {DEVICE} ({torch.cuda.get_device_name(0)})")

class EarlyStopping:
    def __init__(self, patience=5):
        self.patience = patience
        self.best_acc = -np.inf
        self.counter = 0
        self.best_weights = None

    def step(self, val_acc, model):
        if val_acc > self.best_acc:
            self.best_acc = val_acc
            self.counter = 0
            self.best_weights = copy.deepcopy(model.state_dict())  # deep copy — optimizer modifies tensors in-place
        else:
            self.counter += 1
        return self.counter >= self.patience


class MLP(nn.Module):
    # layer_sizes = [input] + [hidden...] + [output]
    # activations: 'relu', 'leakyrelu', 'elu', 'tanh', 'sigmoid'
    # dropout applied after each hidden layer (not output)

    # Factory functions — each call returns a fresh module instance (avoids shared state)
    _ACTIVATION_FACTORIES = {
        'relu':      lambda: nn.ReLU(),
        'leakyrelu': lambda: nn.LeakyReLU(0.01),
        'elu':       lambda: nn.ELU(),
        'tanh':      lambda: nn.Tanh(),
        'sigmoid':   lambda: nn.Sigmoid(),
    }

    def __init__(self, layer_sizes: List[int], activation: str, dropout: float):
        super(MLP, self).__init__()
        act_factory = self._ACTIVATION_FACTORIES.get(activation.lower())
        if act_factory is None:
            raise ValueError(f"Unsupported activation: {activation}")

        layers = []
        for i in range(len(layer_sizes) - 1):
            layers.append(nn.Linear(layer_sizes[i], layer_sizes[i + 1]))
            if i < len(layer_sizes) - 2:          # hidden layers only
                layers.append(act_factory())       # fresh instance per layer
                if dropout > 0:
                    layers.append(nn.Dropout(dropout))
        self.model = nn.Sequential(*layers)

    def forward(self, x):
        return self.model(x)


def train_one_epoch(model, loader, optimizer, criterion):
    model.train()
    total_loss, correct, total = 0.0, 0, 0
    for images, labels in loader:
        images, labels = images.to(DEVICE, non_blocking=True), labels.to(DEVICE, non_blocking=True)
        optimizer.zero_grad()
        out = model(images)
        loss = criterion(out, labels)
        loss.backward()
        optimizer.step()
        total_loss += loss.item() * images.size(0)
        correct += out.argmax(1).eq(labels).sum().item()
        total += labels.size(0)
    return total_loss / total, correct / total


def evaluate(model, loader, criterion):
    model.eval()
    total_loss, correct, total = 0.0, 0, 0
    with torch.no_grad():
        for images, labels in loader:
            images, labels = images.to(DEVICE, non_blocking=True), labels.to(DEVICE, non_blocking=True)
            out = model(images)
            loss = criterion(out, labels)
            total_loss += loss.item() * images.size(0)
            correct += out.argmax(1).eq(labels).sum().item()
            total += labels.size(0)
    return total_loss / total, correct / total


def run_experiment(build_model_fn, build_optimizer_fn, seeds=[42, 123, 456], n_epochs=50):
    # build_optimizer_fn receives the model (not model.parameters()) so it can inspect params
    criterion = nn.CrossEntropyLoss()
    val_accs, epoch_counts, histories = [], [], []
    t0 = time.time()

    for seed in seeds:
        set_seed(seed)
        model = build_model_fn().to(DEVICE)
        optimizer = build_optimizer_fn(model)
        early_stopping = EarlyStopping(patience=5)

        history = {'train_loss': [], 'val_loss': [], 'train_acc': [], 'val_acc': []}
        for epoch in range(n_epochs):
            tr_loss, tr_acc = train_one_epoch(model, train_loader, optimizer, criterion)
            vl_loss, vl_acc = evaluate(model, val_loader, criterion)
            history['train_loss'].append(tr_loss)
            history['train_acc'].append(tr_acc)
            history['val_loss'].append(vl_loss)
            history['val_acc'].append(vl_acc)
            if early_stopping.step(vl_acc, model):
                print(f"  Seed {seed}: early stop @ epoch {epoch + 1}")
                break

        model.load_state_dict(early_stopping.best_weights)
        val_accs.append(early_stopping.best_acc)
        epoch_counts.append(len(history['val_acc']))
        histories.append(history)

    total_wall_time = time.time() - t0
    return (float(np.mean(val_accs)), float(np.std(val_accs)),
            float(np.mean(epoch_counts)), histories, total_wall_time)

def plot_history(history, metric, title, filename, ylabel=None):
    plt.figure(figsize=(10, 5))
    for label, runs in history.items():
        # average over seeds
        max_len = max(len(h[metric]) for h in runs)
        arr = np.full((len(runs), max_len), np.nan)
        for i, h in enumerate(runs):
            arr[i, :len(h[metric])] = h[metric]
        mean = np.nanmean(arr, axis=0)
        plt.plot(mean, label=label)
    plt.xlabel("Epoch")
    plt.ylabel(ylabel or metric)
    plt.title(title)
    plt.legend()
    plt.tight_layout()
    plt.savefig(filename, dpi=150)
    plt.close()

def plot_bar(labels, means, stds, title, filename, ylabel="Val accuracy"):
    plt.figure(figsize=(max(6, len(labels)*1.4), 5))
    x = np.arange(len(labels))
    plt.bar(x, means, yerr=stds, capsize=5)
    plt.xticks(x, labels, rotation=45, ha='right')
    plt.ylabel(ylabel)
    plt.title(title)
    plt.ylim(max(0, min(means) - max(stds)*2), min(1, max(means) + max(stds)*2))
    plt.tight_layout()
    plt.savefig(filename, dpi=150)
    plt.close()

# Phase 2 — Topologies
TOPOLOGIES = {
    "T1 [64]":                    [784, 64, 10],
    "T2 [256,128]":               [784, 256, 128, 10],
    "T3 [512,256,128]":           [784, 512, 256, 128, 10],
    "T4 [1024,512,256,128]":      [784, 1024, 512, 256, 128, 10],
    "T5 [2048,1024,512,256,128]": [784, 2048, 1024, 512, 256, 128, 10],
}

topo_results = {}
topo_histories = {}

for name, sizes in TOPOLOGIES.items():
    print(f"Running topology: {name}")
    build_model_fn = lambda s=sizes: MLP(layer_sizes=s, activation='relu', dropout=0.0)
    build_optimizer_fn = lambda model: optim.Adam(model.parameters(), lr=0.001)

    mu, sd, ep, hists, wt = run_experiment(build_model_fn, build_optimizer_fn)
    topo_results[name] = {"mean_val_acc": mu, "std_val_acc": sd, "mean_epochs": ep, "wall_time": wt}
    topo_histories[name] = hists
    print(f"  val={mu:.4f}±{sd:.4f}  epochs={ep:.1f}  t={wt:.1f}s")

best_topo = max(topo_results, key=lambda k: topo_results[k]['mean_val_acc'])
best_sizes = TOPOLOGIES[best_topo]
print(f"\nBest topology: {best_topo}")

plot_history(topo_histories, 'val_loss', 'Topologies — Validation Loss', 'topology_curves.png', ylabel='Val Loss')
plot_bar(
    list(topo_results.keys()),
    [v['mean_val_acc'] for v in topo_results.values()],
    [v['std_val_acc']  for v in topo_results.values()],
    'Topologies — Val Accuracy', 'topology_bar.png'
)



# Phase 3 — Optimizers
OPTIMIZERS = {
    "Adam":    lambda model: optim.Adam(model.parameters(),    lr=0.001),
    "SGD":     lambda model: optim.SGD(model.parameters(),     lr=0.001, momentum=0.9),
    "RMSprop": lambda model: optim.RMSprop(model.parameters(), lr=0.001),
}

opt_results = {}
opt_histories = {}

for name, build_optimizer_fn in OPTIMIZERS.items():
    print(f"Running optimizer: {name}")
    build_model_fn = lambda: MLP(layer_sizes=best_sizes, activation='relu', dropout=0.0)

    mu, sd, ep, hists, wt = run_experiment(build_model_fn, build_optimizer_fn)
    opt_results[name] = {"mean_val_acc": mu, "std_val_acc": sd, "mean_epochs": ep, "wall_time": wt}
    opt_histories[name] = hists
    print(f"  val={mu:.4f}±{sd:.4f}  epochs={ep:.1f}  t={wt:.1f}s")

best_opt = max(opt_results, key=lambda k: opt_results[k]['mean_val_acc'])
print(f"\nBest optimizer: {best_opt}")

plot_history(opt_histories, 'val_loss', 'Optimizers — Validation Loss', 'optimizer_curves.png', ylabel='Val Loss')
plot_bar(
    list(opt_results.keys()),
    [v['mean_val_acc'] for v in opt_results.values()],
    [v['std_val_acc']  for v in opt_results.values()],
    'Optimizers — Val Accuracy', 'optimizer_bar.png'
)

# Phase 4 — Learning Rates
_OPT_LR_BUILDERS = {
    "Adam":    lambda model, lr: optim.Adam(model.parameters(),    lr=lr),
    "SGD":     lambda model, lr: optim.SGD(model.parameters(),     lr=lr, momentum=0.9),
    "RMSprop": lambda model, lr: optim.RMSprop(model.parameters(), lr=lr),
}

LEARNING_RATES = [0.0001, 0.001, 0.005, 0.01, 0.1]

lr_results = {}
lr_histories = {}

for lr in LEARNING_RATES:
    label = f"lr={lr}"
    print(f"Running {label}")
    build_model_fn = lambda: MLP(layer_sizes=best_sizes, activation='relu', dropout=0.0)
    build_optimizer_fn = lambda model, _lr=lr: _OPT_LR_BUILDERS[best_opt](model, _lr)  # capture lr via default arg

    mu, sd, ep, hists, wt = run_experiment(build_model_fn, build_optimizer_fn)
    lr_results[label] = {"mean_val_acc": mu, "std_val_acc": sd, "mean_epochs": ep, "wall_time": wt}
    lr_histories[label] = hists
    print(f"  val={mu:.4f}±{sd:.4f}  epochs={ep:.1f}")

best_lr_label = max(lr_results, key=lambda k: lr_results[k]['mean_val_acc'])
best_lr = float(best_lr_label.split("=")[1])
print(f"\nBest LR: {best_lr}")

plot_history(lr_histories, 'val_loss', 'Learning Rates — Validation Loss', 'lr_curves.png', ylabel='Val Loss')
plot_bar(
    list(lr_results.keys()),
    [v['mean_val_acc'] for v in lr_results.values()],
    [v['std_val_acc']  for v in lr_results.values()],
    'Learning Rates — Val Accuracy', 'lr_bar.png'
)

# Phase 5 — Activation Functions
ACTIVATIONS = ['relu', 'leakyrelu', 'elu', 'tanh', 'sigmoid']

act_results = {}
act_histories = {}

for act in ACTIVATIONS:
    print(f"Running activation: {act}")
    build_model_fn = lambda _act=act: MLP(layer_sizes=best_sizes, activation=_act, dropout=0.0)
    build_optimizer_fn = lambda model: _OPT_LR_BUILDERS[best_opt](model, best_lr)

    mu, sd, ep, hists, wt = run_experiment(build_model_fn, build_optimizer_fn)
    act_results[act] = {"mean_val_acc": mu, "std_val_acc": sd, "mean_epochs": ep, "wall_time": wt}
    act_histories[act] = hists
    print(f"  val={mu:.4f}±{sd:.4f}  epochs={ep:.1f}")

best_act = max(act_results, key=lambda k: act_results[k]['mean_val_acc'])
print(f"\nBest activation: {best_act}")

plot_history(act_histories, 'val_loss', 'Activations — Validation Loss', 'activation_curves.png', ylabel='Val Loss')
plot_bar(
    ACTIVATIONS,
    [v['mean_val_acc'] for v in act_results.values()],
    [v['std_val_acc']  for v in act_results.values()],
    'Activations — Val Accuracy', 'activation_bar.png'
)

# Phase 6 — Regularization
_OPT_REG_BUILDERS = {
    "Adam":    lambda model, lr, wd: optim.Adam(model.parameters(),    lr=lr, weight_decay=wd),
    "SGD":     lambda model, lr, wd: optim.SGD(model.parameters(),     lr=lr, momentum=0.9, weight_decay=wd),
    "RMSprop": lambda model, lr, wd: optim.RMSprop(model.parameters(), lr=lr, weight_decay=wd),
}

REG_CONFIGS = {
    "None":               {"dropout": 0.0, "weight_decay": 0.0},
    "Dropout 0.3":        {"dropout": 0.3, "weight_decay": 0.0},
    "Dropout 0.5":        {"dropout": 0.5, "weight_decay": 0.0},
    "L2 1e-4":            {"dropout": 0.0, "weight_decay": 1e-4},
    "L2 1e-3":            {"dropout": 0.0, "weight_decay": 1e-3},
    "Dropout0.3+L2 1e-4": {"dropout": 0.3, "weight_decay": 1e-4},
}

reg_results = {}
reg_histories = {}

for name, config in REG_CONFIGS.items():
    print(f"Running regularization: {name}")
    _do = config["dropout"]
    _wd = config["weight_decay"]
    build_model_fn     = lambda _d=_do: MLP(layer_sizes=best_sizes, activation=best_act, dropout=_d)
    build_optimizer_fn = lambda model, _w=_wd: _OPT_REG_BUILDERS[best_opt](model, best_lr, _w)

    mu, sd, ep, hists, wt = run_experiment(build_model_fn, build_optimizer_fn)
    mean_train_acc = float(np.mean([max(h['train_acc']) for h in hists]))  # use hists from results, not reg_histories
    reg_results[name] = {
        "mean_val_acc":   mu,
        "std_val_acc":    sd,
        "mean_train_acc": mean_train_acc,
        "train_val_gap":  round(mean_train_acc - mu, 4),
        "mean_epochs":    ep,
        "wall_time":      wt,
    }
    reg_histories[name] = hists
    print(f"  val={mu:.4f}±{sd:.4f}  train={mean_train_acc:.4f}  gap={mean_train_acc-mu:.4f}")

best_reg = max(reg_results, key=lambda k: reg_results[k]['mean_val_acc'])
best_wd      = REG_CONFIGS[best_reg]["weight_decay"]
best_dropout = REG_CONFIGS[best_reg]["dropout"]
print(f"\nBest regularization: {best_reg}")

plot_history(reg_histories, 'val_loss', 'Regularization — Validation Loss', 'reg_curves.png', ylabel='Val Loss')
plot_bar(
    list(reg_results.keys()),
    [v['mean_val_acc'] for v in reg_results.values()],
    [v['std_val_acc']  for v in reg_results.values()],
    'Regularization — Val Accuracy', 'reg_bar.png'
)

print("=== Final Model ===")
print(f" Topology    : {best_topo}")
print(f" Optimizer   : {best_opt}")
print(f" LR          : {best_lr}")
print(f" Activation  : {best_act}")
print(f" Dropout     : {best_dropout}")
print(f" Weight Decay: {best_wd}")

# Retrain on train + val combined (60k samples)
set_seed(42)
_pin = torch.cuda.is_available()
mnist_trainval   = ConcatDataset([mnist_train, mnist_val])
trainval_loader  = DataLoader(mnist_trainval, batch_size=128, shuffle=True, pin_memory=_pin, num_workers=0)

final_model = MLP(layer_sizes=best_sizes, activation=best_act, dropout=best_dropout).to(DEVICE)
final_optimizer = _OPT_REG_BUILDERS[best_opt](final_model, best_lr, best_wd)
criterion = nn.CrossEntropyLoss()

n_final_epochs = max(30, int(reg_results[best_reg]['mean_epochs']))
for epoch in range(n_final_epochs):
    tr_loss, tr_acc = train_one_epoch(final_model, trainval_loader, final_optimizer, criterion)
    print(f"Epoch {epoch+1}/{n_final_epochs}  train_loss={tr_loss:.4f}  train_acc={tr_acc:.4f}")

# Evaluate on test set — first and only time
final_test_loss, final_test_acc = evaluate(final_model, test_loader, criterion)
print(f"\nFinal test accuracy: {final_test_acc:.4f}")

# Confusion matrix
final_model.eval()
all_preds, all_labels = [], []
with torch.no_grad():
    for X, y in test_loader:
        preds = final_model(X.to(DEVICE)).argmax(1).cpu().numpy()
        all_preds.append(preds)
        all_labels.append(y.numpy())
all_preds  = np.concatenate(all_preds)
all_labels = np.concatenate(all_labels)

cm = confusion_matrix(all_labels, all_preds)
fig, ax = plt.subplots(figsize=(8, 7))
disp = ConfusionMatrixDisplay(confusion_matrix=cm, display_labels=range(10))
disp.plot(ax=ax, cmap='Blues', values_format='d', colorbar=False)
ax.set_title(f"Final Model — Confusion Matrix (test acc={final_test_acc:.4f})")
plt.tight_layout()
plt.savefig('final_confusion_matrix.png', dpi=150)
plt.close()

results_summary = {
    "baseline_logistic_regression": {
        "val_accuracy":  float(accuracy_score(y_val,  log_reg.predict(X_val))),
        "test_accuracy": float(accuracy_score(y_test, log_reg.predict(X_test))),
    },
    "topologies":    topo_results,
    "optimizers":    opt_results,
    "learning_rates": lr_results,
    "activations":   act_results,
    "regularization": reg_results,
    "final_model": {
        "topology":      best_topo,
        "topology_sizes": best_sizes,
        "optimizer":     best_opt,
        "learning_rate": best_lr,
        "activation":    best_act,
        "dropout":       best_dropout,
        "weight_decay":  best_wd,
        "test_accuracy": final_test_acc,
        "seeds":         [42, 123, 456],
    },
}

with open("results_summary.json", "w") as f:
    json.dump(results_summary, f, indent=4)

print("Results saved to results_summary.json")