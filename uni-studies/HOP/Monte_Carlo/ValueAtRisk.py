import numpy as np
import time
import matplotlib.pyplot as plt
from scipy.stats import norm 

def monte_carlo_var(
        mu=0.001, 
        sigma=0.02, 
        n_samples=10000, 
        alpha=0.05):
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

def monte_carlo_var_IS(
    mu_P=0.001, sigma_P=0.02,    # Target (P) parameters
    mu_Q=-0.03, sigma_Q=0.02,    # Proposal (Q) parameters
    n_samples=10000, alpha=0.05):
    """
    Importance Sampling Monte Carlo estimation of Value at Risk (VaR) for a portfolio.

    Parameters:
    - mu_P, sigma_P: Mean and stddev of target distribution P
    - mu_Q, sigma_Q: Mean and stddev of proposal distribution Q
    - n_samples: Number of simulated returns
    - alpha: Confidence level for VaR (e.g., 0.05 → 95% confidence)

    Procedure:
    1. Generate simulated returns from proposal distribution Q.
    2. Compute importance weights: w = p(x) / q(x)
    3. Compute the weighted alpha-percentile (worst-case threshold).

    Returns:
    - var: Estimated Value at Risk
    - ess: Effective Sample Size (ESS) of the weighted samples
    """
    returns = np.random.normal(mu_Q, sigma_Q, n_samples)  # Simulated returns
    p_val = norm.pdf(returns, loc=mu_P, scale=sigma_P)
    q_val = norm.pdf(returns, loc=mu_Q, scale=sigma_Q)
    weights = p_val/q_val
    var = np.percentile(returns, 
                        100 * alpha, 
                        weights=weights, 
                        method='inverted_cdf')
    weights_normalized = weights / np.sum(weights)
    ess = 1 / np.sum(weights_normalized**2)
    
    return var, ess

def main():
    # --- Configuration ---
    N_SAMPLES_PER_RUN = 10000  # (N)
    ALPHA = 0.05

    # Number of times to repeat the *entire* simulation
    N_RUNS = 1000  # (M)

    # Distribution parameters
    MU_P, SIGMA_P = 0.001, 0.02  # Target
    # Calculate heuristic optimal Q parameters
    z_score_alpha = norm.ppf(ALPHA)
    MU_Q = MU_P + z_score_alpha * SIGMA_P
    SIGMA_Q = SIGMA_P * 1.5

    # --- 1. Run the Comparison Loop ---
    results_mc = []
    results_is = []
    results_ess = []

    print(f"Running comparison: {N_RUNS} runs of {N_SAMPLES_PER_RUN} samples each...")
    start_time = time.time()

    for _ in range(N_RUNS):
        # 1. Run Standard MC
        var_mc = monte_carlo_var(MU_P, SIGMA_P, N_SAMPLES_PER_RUN, ALPHA)
        results_mc.append(var_mc)
        
        # 2. Run Importance Sampling MC
        var_is, ess = monte_carlo_var_IS(
            MU_P, SIGMA_P, MU_Q, SIGMA_Q, # type: ignore
            N_SAMPLES_PER_RUN, ALPHA
        )
        results_is.append(var_is)
        results_ess.append(ess)

    end_time = time.time()
    print(f"...Simulation complete. Total time: {end_time - start_time:.2f} seconds.")

    # --- 2. Calculate and Showcase Statistics ---
    results_mc = np.array(results_mc)
    results_is = np.array(results_is)
    mean_ess = np.mean(results_ess)

    # Calculate variance (stability) of the *estimators*
    mean_mc, var_mc, std_mc = np.mean(results_mc), np.var(results_mc), np.std(results_mc)
    mean_is, var_is, std_is = np.mean(results_is), np.var(results_is), np.std(results_is)

    # Calculate Relative Efficiency
    relative_efficiency = var_mc / var_is

    print("\n--- Comparison of VaR Estimators ---")
    print(f"                     | {'Direct MC':<18} | {'Importance Sampling':<20}")
    print(f"---------------------|--------------------|---------------------")
    print(f"Mean VaR Estimate    | {mean_mc:<18.6f} | {mean_is:<20.6f}")    
    print(f"Variance of Estimate | {var_mc:<18.6e} | {var_is:<20.6e}")
    print(f"Std. Dev. of Estimate| {std_mc:<18.6e} | {std_is:<20.6e}")
    print(f"---------------------|--------------------|---------------------")
    print(f"Relative Efficiency  | {'1.0x':<18} | {relative_efficiency:<20.1f}x")
    print(f"Avg. Eff. Sample Size| {'N/A':<18} | {mean_ess:<20.1f} / {N_SAMPLES_PER_RUN}")

    # --- 3. Generate PDFs Visualization ---
    plt.figure(figsize=(8, 6))
    plt.hist(np.random.normal(MU_Q, SIGMA_Q, N_SAMPLES_PER_RUN), 200, density=True, alpha=0.95, label='Q: Proposal')
    plt.hist(np.random.normal(MU_P, SIGMA_P, N_SAMPLES_PER_RUN), 200, density=True, alpha=0.95, label='P: Target')
    plt.title('Probability Density Functions')
    plt.xlabel('Return')
    plt.ylabel('Density')
    plt.legend()
    plt.show()

if __name__ == "__main__":
    main()