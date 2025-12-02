from models import Task, Device, load_data

def build_schedule(tasks:list[Task], devices:list[Device], task_order_indices:list[int]) -> int:
    for d in devices:
        d.usage_log = [] # for fresh start
    
    task_map = {t.name: t for t in tasks}

    for task_idx in task_order_indices:
        task = tasks[task_idx]
        
        # --- Satisfy prerequisites ---
        min_start_time = 0
        for prereq_name in task.prerequisites:
            prereq_task = task_map[prereq_name]

            if prereq_task.start_time is None:
                return 2**31 - 1 
            min_start_time = max(min_start_time, prereq_task.start_time + prereq_task.duration) 
    
        # --- Find Earliest Device Slot ---
        best_device: Device | None = None
        earliest_start = 2**31 - 1
        
        for dev_name in task.devices:
            device = next(d for d in devices if d.name == dev_name)
            
            # Search for the first available gap starting from min_start_time
            current_test_time = min_start_time
            found_slot = False
            
            while current_test_time < 100000: 
                if device.is_available(current_test_time, task.duration, task.parallel):
                    if current_test_time < earliest_start:
                        earliest_start = current_test_time
                        best_device = device
                    found_slot = True
                    break
                else:
                    current_test_time += 1
        
         # --- Step C: Assign Task ---
        if best_device:
            task.start_time = earliest_start
            task.assigned_device = best_device.name
            best_device.assign(earliest_start, task.duration, task.parallel)

    # Calculate Makespan
    makespan = 0
    for t in tasks:
        finish_time = t.start_time + t.duration
        if finish_time > makespan:
            makespan = finish_time
            
    return makespan