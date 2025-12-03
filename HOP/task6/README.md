# Task Scheduling with GRASP

This project implements a task scheduling system using the **Greedy Randomized Adaptive Search Procedure (GRASP)** metaheuristic. It is designed to optimize the execution order of tasks on a set of devices, respecting prerequisites and parallel execution constraints, with the goal of minimizing the total makespan.

## Description

The application schedules a set of tasks onto available devices. Each task has a specific duration, a list of allowed devices, a set of prerequisite tasks that must be completed before it can start, and a flag indicating if it can be run in parallel with other parallel tasks on the same device.

The core of the solution is the GRASP algorithm, which combines a randomized greedy construction phase with a local search improvement phase to find high-quality schedules.

## Features

- **Prerequisite Handling**: Ensures tasks only start after all their dependencies are finished.
- **Device Management**: Assigns tasks to specific devices based on availability.
- **Concurrency Control**: Supports both parallel and exclusive task execution modes on devices.
- **Optimization**: Uses GRASP to minimize the total project duration (makespan).
- **JSON Input**: Loads problem definitions (tasks and devices) from a structured JSON file.

## Project Structure

- `GRASP.py`: The main entry point. Implements the GRASP metaheuristic (Construction and Local Search phases).
- `scheduler.py`: Contains the `build_schedule` function which deterministically constructs a schedule from a given task order.
- `models.py`: Defines the `Task` and `Device` classes and handles data loading.
- `a2v6.json`: Input data file containing the list of devices and tasks.

## Installation

1. Ensure you have Python 3.x installed.
2. No external dependencies are required beyond the standard library.

## Usage

To run the optimization, execute the `GRASP.py` script from the root of the repository or the folder:

```bash
python HOP/task6/GRASP.py
```

*Note: You may need to adjust the file path in `GRASP.py` depending on your working directory.*

## Results

Example output from a run with 50 iterations:

```text
Starting GRASP with 50 iterations...
New Best found at iter 0: 318 mins
New Best found at iter 1: 314 mins
New Best found at iter 2: 299 mins
New Best found at iter 5: 293 mins
New Best found at iter 25: 281 mins
Best Makespan: 281
```

## Algorithm Details

The solution employs the **GRASP** metaheuristic, which consists of two main phases repeated for a number of iterations:

### 1. Construction Phase
- Builds a feasible solution step-by-step.
- Maintains a list of "available" tasks (those whose prerequisites are met).
- Uses a **Restricted Candidate List (RCL)** to select the next task.
- The selection is greedy (based on task duration) but randomized by an `alpha` parameter (0.0 to 1.0) to ensure diversity in solutions.

### 2. Local Search Phase
- Takes the solution constructed in the first phase and tries to improve it.
- Iteratively swaps adjacent tasks in the execution order.
- If a swap results in a lower makespan, the change is kept.
- This continues until no further improvements can be made (local optimum).

## Roadmap

The following optimization methods are planned for future implementation to improve solution quality and escape local optima:

### Simulated Annealing (SA) 
A trajectory-based method inspired by thermodynamics

**Strategy**: Starts with a valid schedule and iteratively makes small perturbations.
 
**Goal**: Unlike standard hill-climbing, SA accepts worse solutions with a probability that decreases over time (cooling). This allows the solver to escape local optima and explore a broader area of the search space.

### Genetic Algorithms (GA) 
A population-based evolutionary strategy

**Strategy**: Maintains a pool of candidate schedules.

**Operators**: Uses Crossover to combine partial schedules from two parents and Mutation to introduce random changes. This approach is particularly effective for large search spaces where decomposing the problem is beneficial

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
