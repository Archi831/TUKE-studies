# Task Scheduling Optimization

This project implements a task scheduling system using metaheuristic algorithms to optimize the execution order of tasks on a set of devices. It respects prerequisites and parallel execution constraints, with the goal of minimizing the total makespan.

## Description

The application schedules a set of tasks onto available devices. Each task has a specific duration, a list of allowed devices, a set of prerequisite tasks that must be completed before it can start, and a flag indicating if it can be run in parallel with other parallel tasks on the same device.

The solution currently implements three algorithms:
1. **GRASP (Greedy Randomized Adaptive Search Procedure)**: Combines a randomized greedy construction phase with a local search improvement phase.
2. **Simulated Annealing**: A probabilistic technique for approximating the global optimum of a given function.
3. **Genetic Algorithm**: An evolutionary algorithm that uses selection, crossover, and mutation to evolve a population of schedules.

## Features

- **Prerequisite Handling**: Ensures tasks only start after all their dependencies are finished.
- **Device Management**: Assigns tasks to specific devices based on availability.
- **Concurrency Control**: Supports both parallel and exclusive task execution modes on devices.
- **Optimization**: Uses GRASP to minimize the total project duration (makespan).
- **JSON Input**: Loads problem definitions (tasks and devices) from a structured JSON file.

## Project Structure

- `GRASP.py`: Implements the GRASP metaheuristic (Construction and Local Search phases).
- `simulatedAnnealing.py`: Implements the Simulated Annealing metaheuristic.
- `GeneticAlgorithm.py`: Implements the Genetic Algorithm metaheuristic.
- `scheduler.py`: Contains the `build_schedule` function which deterministically constructs a schedule from a given task order.
- `models.py`: Defines the `Task` and `Device` classes and handles data loading.
- `a2v6.json`: Input data file containing the list of devices and tasks.

## Installation

1. Ensure you have Python 3.x installed.
2. No external dependencies are required beyond the standard library.

## Usage

To run the optimization, execute the desired script from the root of the repository:

**Run GRASP:**
```bash
python HOP/task6/GRASP.py
```

**Run Simulated Annealing:**
```bash
python HOP/task6/simulatedAnnealing.py
```

**Run Genetic Algorithm:**
```bash
python HOP/task6/GeneticAlgorithm.py
```

*Note: You may need to adjust the file paths in the scripts depending on your working directory.*

## Results

### GRASP
Example output from a run with 50 iterations:

```text
Starting GRASP with 50 iterations...
New Best found at iter 0: 263.0 mins
New Best found at iter 1: 247.0 mins
New Best found at iter 2: 246.0 mins
New Best found at iter 6: 243.0 mins
New Best found at iter 23: 238.0 mins
New Best found at iter 34: 232.0 mins
Best Makespan: 232.0
```

### Simulated Annealing
Example output from a run with 10,000 iterations:

```text
Starting Simulated Annealing with initial makespan: 2147483647 mins
New Best found at iter 1620: 330 mins, with temp 1000.0000
New Best found at iter 1627: 329 mins, with temp 993.0210
New Best found at iter 1639: 313 mins, with temp 981.1700
New Best found at iter 1684: 297 mins, with temp 937.9750
New Best found at iter 1686: 286 mins, with temp 936.1000
New Best found at iter 1691: 281 mins, with temp 931.4288
New Best found at iter 1711: 264 mins, with temp 912.9761
New Best found at iter 1729: 262 mins, with temp 896.6815
New Best found at iter 3109: 261 mins, with temp 225.4301
New Best found at iter 5779: 247 mins, with temp 15.5907
New Best found at iter 8199: 237 mins, with temp 1.3847
New Best found at iter 9717: 235 mins, with temp 0.3032
Best Makespan: 235 mins
```

### Genetic Algorithm
Example output from a run with population size 200 and 100 generations:

```text
Initial Best: 281.0
Gen 0: New Best 259.0
Gen 1: New Best 256.0
Gen 3: New Best 250.0
Gen 15: New Best 246.0
Gen 23: New Best 232.0
Best Makespan: 232.0
```

## Algorithm Details

### GRASP
The solution employs the **GRASP** metaheuristic, which consists of two main phases repeated for a number of iterations:

#### 1. Construction Phase
- Builds a feasible solution step-by-step.
- Maintains a list of "available" tasks (those whose prerequisites are met).
- Uses a **Restricted Candidate List (RCL)** to select the next task.
- The selection is greedy (based on task duration) but randomized by an `alpha` parameter (0.0 to 1.0) to ensure diversity in solutions.

#### 2. Local Search Phase
- Takes the solution constructed in the first phase and tries to improve it.
- Iteratively swaps adjacent tasks in the execution order.
- If a swap results in a lower makespan, the change is kept.
- This continues until no further improvements can be made (local optimum).

### Simulated Annealing
A trajectory-based method inspired by thermodynamics.

- **Strategy**: Starts with a valid schedule and iteratively makes small perturbations (swapping two random tasks).
- **Cooling Schedule**: Uses a geometric cooling schedule (`temp *= cooling_rate`) to gradually reduce the probability of accepting worse solutions.
- **Acceptance Probability**: Worse solutions are accepted with probability $P = e^{-\Delta / T}$, allowing the algorithm to escape local optima.

### Genetic Algorithm
A population-based evolutionary strategy.

- **Representation**: Permutation of task indices.
- **Selection**: Tournament Selection (k=3) to choose parents for the next generation.
- **Crossover**: Ordered Crossover (OX) to combine parents while preserving relative task order and validity.
- **Mutation**: Swap Mutation (swaps two random tasks) to introduce diversity.
- **Elitism**: The best individual found so far is always preserved in the next generation.

## Roadmap

Currently all initially planned algorithms have been implemented.

## Input Format (`a2v6.json`)

The input file should be a JSON object with two main keys: `devices` and `tasks`.

```json
{
  "devices": ["Device1", "Device2"],
  "tasks": [
    {
      "name": "TaskA",
      "duration": 10,
      "devices": ["Device1"],
      "prerequisites": [],
      "parallel": true
    },
    {
      "name": "TaskB",
      "duration": 20,
      "devices": ["Device1", "Device2"],
      "prerequisites": ["TaskA"],
      "parallel": false
    }
  ]
}
```
