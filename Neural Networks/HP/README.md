# Neural Networks - Hyperparameter Testing (HP)

This folder contains a complete hyperparameter testing assignment for feed-forward neural networks on MNIST.

## Goal

Systematically and reproducibly evaluate how different hyperparameters affect model performance:

- topology (network depth/width)
- optimizer
- learning rate
- activation function
- regularization (dropout, L2)

A logistic regression baseline is included for comparison.

## Main Files

- `Testovanie_Lobodiuchenko.py` - full experiment pipeline (EDA, baseline, training, sweeps, final model)
- `results_summary.json` - aggregated experiment results (means/std over multiple seeds)
- `Testovanie_Lobodiuchenko.pdf` - final report

## Dataset and Split

- Dataset: MNIST (downloaded automatically by `torchvision`)
- Train/Validation split: 50,000 / 10,000
- Test set: official MNIST test split (10,000)

## Reproducibility

The script enforces reproducibility by:

- fixed seeds (default: 42, 123, 456)
- deterministic PyTorch/CUDA settings
- identical data split and metric pipeline across all experiments

## Environment

Minimum Python dependencies:

- `torch`
- `torchvision`
- `numpy`
- `matplotlib`
- `seaborn`
- `scikit-learn`

Install example:

```bash
pip install torch torchvision numpy matplotlib seaborn scikit-learn
```

## Run

From this folder:

```bash
python Testovanie_Lobodiuchenko.py
```

Note: the script currently requires a CUDA GPU and will stop with an error if CUDA is not available.

## Key Results (from `results_summary.json`)

- Baseline (Logistic Regression):
  - validation accuracy: 0.9175
  - test accuracy: 0.9243
- Best final model:
  - topology: T5 `[784, 2048, 1024, 512, 256, 128, 10]`
  - optimizer: RMSprop
  - learning rate: 0.001
  - activation: ReLU
  - regularization: Dropout 0.3
  - test accuracy: 0.9863
