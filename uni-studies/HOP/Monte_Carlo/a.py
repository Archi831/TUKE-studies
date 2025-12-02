import numpy as np
import pandas as pd
import time
import matplotlib.pyplot as plt
from scipy.stats import norm 
# Problem 1: Estimation of Pi
def monte_carlo_pi(n_samples=10000):
    """
    Monte Carlo estimation of π using random points in a unit square.
    
    Parameters:
    - n_samples: Number of random points to generate
    
    Procedure:
    1. Generate x, y coordinates uniformly in [0,1].
    2. Count points inside the unit circle (x^2 + y^2 <= 1).
    3. Estimate π using formula: pi ≈ 4 * (inside / n_samples)
    
    Returns:
    - pi_value: Approximated value of π
    """
    x = np.random.rand(n_samples)  
    y = np.random.rand(n_samples)  
    inside = np.sum(x**2 + y**2 <= 1)  # Points inside circle
    pi_value = 4 * inside / n_samples  # π estimation formula
    return pi_value

# Importance sampling
def g(x,y):
    return np.where(x**2 + y**2 > 1, 0, 1)

def monte_carlo_pi_Importance_Sampling(g, N):

    x = 1 - np.sqrt(np.random.rand(N))
    y = 1 - np.sqrt(np.random.rand(N))

    total_value = 0
    p_val = 1
    q_val = 4 * (1 - x) * (1 - y)
    V_val = g(x,y) * (p_val/q_val)
    total_value = np.sum(V_val)
    return 4 * total_value/N


# Problem 2: Value at Risk (VaR) estimation
def monte_carlo_var(mu=0.001, sigma=0.02, n_samples=10000, alpha=0.05):
    """
    Monte Carlo estimation of Value at Risk (VaR) for a portfolio.
    
    Parameters:
    - mu: Expected mean daily return
    - sigma: Standard deviation (volatility) of returns
    - n_samples: Number of simulated returns
    - alpha: Confidence level for VaR (e.g., 0.05 → 95% confidence)
    
    Procedure:
    1. Generate simulated returns from normal distribution with mu, sigma.
    2. Compute the alpha-percentile (worst-case threshold).
    
    Returns:
    - var: Estimated Value at Risk
    """
    returns = np.random.normal(mu, sigma, n_samples)  # Simulated returns
    var = np.percentile(returns, 100 * alpha)  # Compute alpha-percentile
    return var

def monte_carlo_var_Importance_Sampling(mu=-0.03, sigma=0.02, n_samples=10000, alpha=0.05):
    returns = np.random.normal(mu, sigma, n_samples)  # Simulated returns
    p_val = norm.pdf(returns, loc=0.001, scale=0.02)
    q_val = norm.pdf(returns, loc=-0.03, scale=0.02)
    weights = p_val/q_val
    var = np.percentile(returns, 
                        100 * alpha, 
                        weights=weights, 
                        method='inverted_cdf')
    return var




# Run experiments for multiple sample sizes
def run_experiments():
    """
    Run repeated Monte Carlo simulations to check stability of results.
    
    Procedure:
    1. Define list of sample sizes for testing (e.g., 10k, 100k, 1M).
    2. For each sample size:
        a. Run 5 repetitions of π estimation.
        b. Run 5 repetitions of VaR estimation.
        c. Compute mean and standard deviation of results.
    3. Store results in a pandas DataFrame for summary and export.
    
    Returns:
    - DataFrame containing averages and standard deviations of π and VaR
    """
    sample_sizes = [10000, 100000, 1000000]  # Sample sizes to test
    rang = 20
    resultsPI = []
    resultsVAR = []
    for n in sample_sizes:

        start_time = time.time()
        pi_results = [monte_carlo_pi(n) for _ in range(rang)]  # π simulations
        end_time = time.time()
        execution_time_PI = end_time - start_time

        start_time = time.time()
        pi_IS_results = [monte_carlo_pi_Importance_Sampling(g, n) for _ in range(rang)]
        end_time = time.time()
        execution_time_PI_IS = end_time - start_time

        start_time = time.time()
        var_results = [monte_carlo_var(n_samples=n) for _ in range(rang)]  # VaR simulations
        end_time = time.time()
        execution_time_VAR = end_time - start_time

        start_time = time.time()
        var_IS_results = [monte_carlo_var_Importance_Sampling(n_samples=n) for _ in range(rang)]
        end_time = time.time()
        execution_time_VAR_IS = end_time - start_time

        resultsPI.append({
            "Samples": n,
            "Pi_avg": np.mean(pi_results),  
            "Pi_std": np.std(pi_results),  
            "Pi_time": execution_time_PI,
            "Pi_IS_avg": np.mean(pi_IS_results),  
            "Pi_IS_std": np.std(pi_IS_results), 
            "Pi_time_IS": execution_time_PI_IS,
        })

        resultsVAR.append({
            "Samples": n,
            "Var_avg": np.mean(var_results),
            "Var_std": np.std(var_results),
            "Var_time": execution_time_VAR,
            "Var_IS_avg": np.mean(var_IS_results),
            "Var_IS_std": np.std(var_IS_results),
            "Var_IS_time": execution_time_VAR_IS
        })
    return pd.DataFrame(resultsPI), pd.DataFrame(resultsVAR)



tablePI, tableVar = run_experiments() 
print("Monte Carlo PI Results")
print(tablePI)  #
print(tableVar)
tablePI.to_csv("monte_carlo_results.csv", index=False)  # Save results\
tableVar.to_csv("varIS.csv", index=False)