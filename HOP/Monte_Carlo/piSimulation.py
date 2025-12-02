import random
import matplotlib.pyplot as plt
from matplotlib.patches import Circle
import multiprocessing
import time

def simulate_points(num_dots):
    count_inside = 0
    for _ in range(num_dots):
        x = random.uniform(0, 2)
        y = random.uniform(0, 2)
        if (x - 1)**2 + (y - 1)**2 <= 1:
            count_inside += 1
    return count_inside

def main():
    total_dots = 10_000_000
    
    num_processes = multiprocessing.cpu_count()
    print(f"Using {num_processes} processes.")

    dots_per_process = [total_dots // num_processes] * num_processes
    for i in range(total_dots % num_processes):
        dots_per_process[i] += 1

    start_time = time.time()

    with multiprocessing.Pool(processes=num_processes) as pool:
        results = pool.map(simulate_points, dots_per_process)

    total_inside = sum(results)
    
    end_time = time.time()

    pi_estimate = (total_inside / total_dots) * 4
    
    print(f"Total dots: {total_dots}")
    print(f"Dots inside circle: {total_inside}")
    print(f"Pi estimate: {pi_estimate}")
    print(f"Calculation finished in {end_time - start_time:.4f} seconds.")

    plot_sample_size = 10000 
    
    inside_dots_for_plot = []
    outside_dots_for_plot = []

    for _ in range(plot_sample_size):
        x, y = random.uniform(0, 2), random.uniform(0, 2)
        if (x - 1)**2 + (y - 1)**2 <= 1:
            inside_dots_for_plot.append((x, y))
        else:
            outside_dots_for_plot.append((x, y))

    figure, axes = plt.subplots()
    drawing_uncolored_circle = Circle((1, 1), 1, fill=False, color='black')
    axes.add_patch(drawing_uncolored_circle)

    if inside_dots_for_plot:
        axes.scatter(*zip(*inside_dots_for_plot), c='blue', s=1, label='Inside')
    if outside_dots_for_plot:
        axes.scatter(*zip(*outside_dots_for_plot), c='red', s=1, label='Outside')

    axes.set_aspect('equal')
    axes.set_xlim(0, 2)
    axes.set_ylim(0, 2)
    plt.title(f'Monte Carlo Pi Simulation (Plotting {plot_sample_size} samples)')
    plt.legend()
    print("Showing plot...")
    plt.show()


if __name__ == '__main__':
    main()