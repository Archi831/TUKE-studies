import math 
import random
from models import Task, Device, load_data, save_output
from scheduler import build_schedule, generate_random_topological_sort

def create_neighbor(current_order: list[int]) -> list[int]:
    """Generate a neighboring solution by swapping two tasks."""
    neighbor_order = list(current_order)
    i, j = random.sample(range(len(current_order)), 2)
    neighbor_order[i], neighbor_order[j] = neighbor_order[j], neighbor_order[i]
    return neighbor_order

def should_accept(delta: float, temperature: float) -> bool:
    """Decide whether to accept the new solution."""
    if delta < 0:
        return True
    elif temperature > 1e-5:
        acceptance_prob = math.exp(-delta / temperature)
        return random.uniform(0, 1) < acceptance_prob
    return False

def simulated_annealing(tasks:list[Task], devices:list[Device], initial_temp=1000, cooling_rate=0.999, max_iterations=10_000) -> tuple[list[int], float]:
    """
    Simulated Annealing algorithm to optimize task scheduling.
    """

    best_start_order = list(range(len(tasks)))
    best_start_makespan = float('inf')
    
    for _ in range(100):
        order = generate_random_topological_sort(tasks)
        makespan = build_schedule(tasks, devices, order)
        if makespan < best_start_makespan:
            best_start_makespan = makespan
            best_start_order = order

    current_order = best_start_order
    current_makespan = best_start_makespan

    best_order = list(current_order)
    best_makespan = current_makespan

    temp = initial_temp
    print(f"Starting Simulated Annealing with initial makespan: {current_makespan} mins")

    for iter in range(max_iterations):
        neighbor_order = create_neighbor(current_order)
        neighbor_makespan = build_schedule(tasks, devices, neighbor_order)

        if neighbor_makespan == float('inf'):
            continue

        delta = neighbor_makespan - current_makespan

        if should_accept(delta, temp):
            current_order = neighbor_order
            current_makespan = neighbor_makespan

            if current_makespan < best_makespan:
                best_order = list(current_order)
                best_makespan = current_makespan
                print(f"New Best found at iter {iter}: {best_makespan} mins, with temp {temp:.4f}")

        temp *= cooling_rate
    return best_order, best_makespan

if __name__ == "__main__":
    tasks, device_names = load_data("HOP\\task6\\large_dataset.json")
    devices = [Device(name) for name in device_names]

    best_order, best_makespan = simulated_annealing(tasks, devices)
    build_schedule(tasks, devices, best_order)
    save_output(tasks, filename="HOP\\task6\\simulated_annealing_output.csv")
    print(f"Best Makespan: {best_makespan} mins")