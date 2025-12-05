import random
from scheduler import build_schedule, generate_random_topological_sort
from models import Task, Device, load_data

def order_crossover(parent1 : list[int], parent2: list[int]) -> list[int]:
    """
    Implements Ordered Crossover (OX) for permutation problems.
    Preserves the relative order of tasks from parent2 while keeping a slice from parent1.
    """
    size = len(parent1)
    child = [-1] * size
    
    start, end = sorted(random.sample(range(size), 2))
    
    child[start:end] = parent1[start:end]
    
    current_pos = end
    for task in parent2:
        if task not in child:
            if current_pos >= size:
                current_pos = 0
            child[current_pos] = task
            current_pos += 1
            
    return child

def tournament_selection(population : list[dict], k=3) -> list[int]:
    """Selects the best individual from k random samples."""
    selected = random.sample(population, k)
    # Sort by fitness which is makespan in our problem
    selected.sort(key=lambda x: x['makespan'])
    return selected[0]["order"]

def genetic_algorithm(tasks : list[Task], devices: list[Device], pop_size=100, generations=50, mutation_rate=0.1):
    """
    Genetic algorithm to optimize task scheduling.
    """
    population = []
    
    for _ in range(pop_size):
        order = generate_random_topological_sort(tasks)
        makespan = build_schedule(tasks, devices, order)
        population.append({'order': order, 'makespan': makespan})

    global_best = min(population, key=lambda x: x['makespan'])
    print(f"Initial Best: {global_best['makespan']}")

    for gen in range(generations):
        print(f"Generation {gen}...")
        new_population = []
        
        # Keep the absolute best found so far
        new_population.append(global_best)
        
        # Generate the rest of the new population
        while len(new_population) < pop_size:
            parent1 = tournament_selection(population)
            parent2 = tournament_selection(population)
            
            child_order = order_crossover(parent1, parent2)
            
            # Mutation - Swap
            if random.random() < mutation_rate:
                idx1, idx2 = random.sample(range(len(child_order)), 2)
                child_order[idx1], child_order[idx2] = child_order[idx2], child_order[idx1]
            
            makespan = build_schedule(tasks, devices, child_order)
            new_population.append({'order': child_order, 'makespan': makespan})
            
        population = new_population
        
        # Update global best
        current_best = min(population, key=lambda x: x['makespan'])
        if current_best['makespan'] < global_best['makespan']:
            global_best = current_best
            print(f"Gen {gen}: New Best {global_best['makespan']}")

    return global_best['order'], global_best['makespan']

if __name__ == "__main__":
    tasks, device_names = load_data("HOP\\task6\\large_dataset.json")
    devices = [Device(name) for name in device_names]

    best_order, best_makespan = genetic_algorithm(tasks, devices, pop_size=200, generations=10, mutation_rate=0.2)
    print("Best Makespan:", best_makespan)