import random
from models import Task, Device, load_data
from scheduler import build_schedule
"""
Greedy Randomized Adaptive Search Procedure
Chapter 2.8 of "Clever Algorithms"
"""
def get_available_tasks(tasks : list[Task], scheduled_names: set[str]) -> list[int]:
    """Identify tasks whose prerequisites are met."""
    candidates = []
    for i, task in enumerate(tasks):
        if task.name in scheduled_names:
            continue
        if all(p in scheduled_names for p in task.prerequisites):
            candidates.append(i)
    return candidates

def grasp_construction(tasks: list[Task], alpha=0.3) -> list[int]:
    """
    Builds a task execution order using Restricted Candidate List (RCL).
    """
    scheduled_names = set()
    task_order_indices = []
    
    while len(task_order_indices) < len(tasks):
        candidate_indices = get_available_tasks(tasks, scheduled_names)
        
        if not candidate_indices:
            break 
            
        # Score Candidates based on duration
        scores = [tasks[i].duration for i in candidate_indices]
        min_score = min(scores)
        max_score = max(scores)
        
        # Build RCL
        # Threshold: allow tasks within alpha% of the best score
        threshold = min_score + alpha * (max_score - min_score) # lower is better
        
        rcl = [i for i, score in zip(candidate_indices, scores) 
               if score <= threshold]
        
        # Select Randomly from RCL
        selected_idx = random.choice(rcl)
        
        task_order_indices.append(selected_idx)
        scheduled_names.add(tasks[selected_idx].name)
        
    return task_order_indices

def local_search(tasks: list[Task], devices: list[Device], current_order: list[int], current_makespan: float) -> tuple[list[int], float]:
    """
    Tries to improve the schedule by swapping adjacent tasks in the priority list.
    """
    improved_order = list(current_order)
    improved_makespan = current_makespan
    
    for i in range(len(improved_order) - 1):
        neighbor_order = list(improved_order)
        # Swap adjacent tasks
        neighbor_order[i], neighbor_order[i+1] = neighbor_order[i+1], neighbor_order[i]
        new_makespan = build_schedule(tasks, devices, neighbor_order)
        if new_makespan != 2**31-1 and new_makespan < improved_makespan:
            return neighbor_order, new_makespan
            
    return improved_order, improved_makespan

def run_grasp(tasks: list[Task], devices: list[Device], max_iterations=100, alpha=0.2) -> tuple[list[int], float]:
    """
    Main GRASP optimization loop.
    """
    best_order = list(range(len(tasks)))
    best_makespan = float('inf')
    
    print(f"Starting GRASP with {max_iterations} iterations...")
    
    for i in range(max_iterations):
        candidate_order = grasp_construction(tasks, alpha)
        candidate_makespan = build_schedule(tasks, devices, candidate_order)
        
        if candidate_makespan == float('inf'):
            continue # Invalid schedule, skip
            
        # Local Search
        while True:
            improved_order, improved_makespan = local_search(
                tasks, devices, candidate_order, candidate_makespan
            )
            if improved_makespan < candidate_makespan:
                candidate_order = improved_order
                candidate_makespan = improved_makespan
            else:
                break # Local optimum
        
        # Update Global Best
        if candidate_makespan < best_makespan:
            best_makespan = candidate_makespan
            best_order = candidate_order[:]
            print(f"New Best found at iter {i}: {best_makespan} mins")
            
    return best_order, best_makespan

if __name__ == "__main__":
    tasks, device_names = load_data("HOP\\task6\\a2v6.json")
    devices = [Device(name) for name in device_names]
    best_order, best_makespan = run_grasp(tasks, devices, max_iterations=50, alpha=0.3)
    print("Best Makespan:", best_makespan)