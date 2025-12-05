import json

class Task:
    def __init__(self, name, duration, devices, prerequisites, parallel):
        self.name = name
        self.duration = duration
        self.devices = devices
        self.prerequisites = prerequisites
        self.parallel = parallel

        self.start_time : float | None = None
        self.assigned_device = None
    
class Device:
    def __init__(self, name):
        self.name = name
        # Stores: start_time, end_time, is_parallel
        self.usage_log = []

    def is_available(self, proposed_start, duration, task_is_parallel):
        """
        Checks if the device can accept a task at the proposed time.
        Allows parallel execution if both are tagged as is_parallel.
        """
        proposed_end = proposed_start + duration
        
        for (busy_start, busy_end, busy_is_parallel) in self.usage_log:
            # Check for overlap
            if max(proposed_start, busy_start) < min(proposed_end, busy_end):
                # Unless not parallel
                if not (task_is_parallel and busy_is_parallel):
                    return False
        return True
    
    def assign(self, start_time, duration, task_is_parallel):
        """Reserves the time slot on this device."""
        self.usage_log.append((start_time, start_time + duration, task_is_parallel))
        self.usage_log.sort(key=lambda x: x)

def load_data(filename):
    with open(filename, 'r') as f:
        data = json.load(f)

    all_tasks = []
    device_list = data['devices']
    for t in data['tasks']:
        task = Task(
            name=t['name'],
            duration=t['duration'],
            devices=[i for i in t['devices']],
            prerequisites=t['prerequisites'],
            parallel=t['parallel']
        )
        all_tasks.append(task)
    return all_tasks, device_list