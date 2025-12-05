import json
import random
import os

def generate_large_dataset(filename="large_dataset.json", num_devices=10, num_tasks=100):
    """
    Generates a synthetic dataset with random tasks and specific edge cases.
    """
    devices = [f"Device_{i}" for i in range(num_devices)]
    tasks = []

    # Helper to create a task dictionary
    def create_task(name, duration, allowed_devices, prerequisites, parallel):
        return {
            "name": name,
            "duration": duration,
            "devices": allowed_devices,
            "prerequisites": prerequisites,
            "parallel": parallel
        }

    # --- 1. Random Tasks (Bulk of the dataset) ---
    # To avoid cyclic dependencies, tasks only depend on previously created tasks (lower indices).
    # We reserve some count for specific edge cases later.
    random_count = num_tasks - 50 
    for i in range(random_count):
        name = f"Task_{i}"
        duration = random.randint(10, 100)
        
        # Pick 1 to 3 random devices
        num_devs = random.randint(1, 3)
        allowed_devices = random.sample(devices, num_devs)
        
        # Prerequisites: 20% chance to have prerequisites from existing tasks
        prereqs = []
        if i > 0 and random.random() < 0.2:
            num_prereqs = random.randint(1, min(3, i))
            # Pick random indices less than i
            prereq_indices = random.sample(range(i), num_prereqs)
            prereqs = [tasks[idx]["name"] for idx in prereq_indices]
            
        parallel = random.choice([True, False])
        
        tasks.append(create_task(name, duration, allowed_devices, prereqs, parallel))

    current_count = len(tasks)

    # --- 2. Edge Case: Long Sequential Chain (Dependency Hell) ---
    # Task A -> Task B -> Task C ... 
    # This forces the algorithm to respect order and prevents parallel execution of this chain.
    chain_length = 20
    for i in range(chain_length):
        name = f"Chain_Task_{i}"
        duration = random.randint(20, 50)
        allowed_devices = random.sample(devices, 2) # Flexible devices
        
        prereqs = []
        if i > 0:
            prereqs = [f"Chain_Task_{i-1}"]
        elif current_count > 0:
             # Link start of chain to a random previous task to integrate it into the graph
             prereqs = [tasks[random.randint(0, current_count-1)]["name"]]
             
        parallel = False # Force sequential
        tasks.append(create_task(name, duration, allowed_devices, prereqs, parallel))
    
    current_count = len(tasks)

    # --- 3. Edge Case: Bottleneck Device ---
    # Many tasks competing for one specific device.
    # This tests how well the algorithm handles resource scarcity.
    bottleneck_device = devices[0]
    for i in range(15):
        name = f"Bottleneck_Task_{i}"
        duration = random.randint(30, 60)
        allowed_devices = [bottleneck_device]
        prereqs = [] # Independent
        parallel = False # Exclusive access needed
        tasks.append(create_task(name, duration, allowed_devices, prereqs, parallel))

    current_count = len(tasks)

    # --- 4. Edge Case: High Parallelism Burst ---
    # Many short tasks on one device that allows parallel execution.
    # Algorithms should stack these efficiently.
    parallel_device = devices[1]
    for i in range(15):
        name = f"Parallel_Task_{i}"
        duration = random.randint(5, 15)
        allowed_devices = [parallel_device]
        prereqs = []
        parallel = True
        tasks.append(create_task(name, duration, allowed_devices, prereqs, parallel))

    # Construct final JSON structure
    data = {
        "devices": devices,
        "tasks": tasks
    }

    # Ensure directory exists
    os.makedirs(os.path.dirname(filename), exist_ok=True)

    with open(filename, 'w') as f:
        json.dump(data, f, indent=2)
    
    print(f"Generated {len(tasks)} tasks and {len(devices)} devices in {filename}")

if __name__ == "__main__":
    # Generates the file in the same folder structure as your other inputs
    generate_large_dataset("HOP\\task6\\large_dataset.json")
