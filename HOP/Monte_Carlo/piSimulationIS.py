import random
from math import sqrt
import time
import matplotlib.pyplot as plt
from matplotlib.patches import Circle
N = 10_000

def g(x,y):
    if(x**2 + y**2 > 1):
        return 0
    else:
        return 1

def compute_monte_carlo_value(g, N):
    total_value = 0
    p_val = 1
    for i in range(N):
        x = 1 - sqrt(random.uniform(0,1))
        y = 1 - sqrt(random.uniform(0,1))
        q_val = 4 * (1 - x) * (1 - y)
        V_val = g(x,y) * (p_val/q_val)
        total_value += V_val
    return 4 * total_value/N

def main(N, g, compute_monte_carlo_value):
    start_time = time.time()

    print("Sampling", N, "times with Importance Sampling")
    estimates = []
    for i in range(100):
        pi_estimate = compute_monte_carlo_value(g, N)
        estimates.append(pi_estimate)

#calculate average, variance and standard deviation
    pi_estimate = sum(estimates)/len(estimates)
    pi_variance = sum((x - pi_estimate) ** 2 for x in estimates) / len(estimates)
    pi_stddev = pi_variance ** 0.5

    end_time = time.time()
    execution_time = end_time - start_time

    print("Execution time:", execution_time, "seconds")
    print("Pi estimate:", pi_estimate)
    print("Variance:", pi_variance)
    print("Standard Deviation:", pi_stddev)

if __name__ == "__main__":
    main(N, g, compute_monte_carlo_value)
