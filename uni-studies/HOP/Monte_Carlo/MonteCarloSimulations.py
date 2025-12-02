import random
import time
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm
from math import sqrt

# --- Problem 1: Estimating Pi ---

def g_pi(x, y):
    """Indicator function for the unit circle."""
    return 1 if x**2 + y**2 <= 1 else 0

def pi_direct_sampling(n_samples):
    """Estimates Pi using Direct Monte Carlo sampling."""
    total_value = 0
    for _ in range(n_samples):
        x = random.uniform(0, 1)
        y = random.uniform(0, 1)
        total_value += g_pi(x, y)
    return 4 * total_value / n_samples

def pi_importance_sampling(n_samples):
    """Estimates Pi using Importance Sampling."""
    total_value = 0
    p_val = 1  # p(x) is uniform, density is 1 over the 1x1 square
    for _ in range(n_samples):
        # Sample from a proposal distribution that concentrates points near (0,0)
        x = 1 - sqrt(random.uniform(0, 1))
        y = 1 - sqrt(random.uniform(0, 1))
        # PDF of the proposal distribution q(x,y) = 4(1-x)(1-y)
        q_val = 4 * (1 - x) * (1 - y)
        weight = p_val / q_val
        total_value += g_pi(x, y) * weight
    # The expectation of the weighted sum is pi/4
    return 4 * total_value / n_samples

def run_pi_comparison(n_runs, n_samples):
    """Runs and compares DMC and IS for Pi estimation."""
    print("--- 1. Running Pi Estimation Comparison ---")
    print(f"Running {n_runs} runs of {n_samples} samples each...")
    
    estimates_dmc = []
    estimates_is = []
    
    start_time = time.time()
    for _ in range(n_runs):
        estimates_dmc.append(pi_direct_sampling(n_samples))
        estimates_is.append(pi_importance_sampling(n_samples))
    end_time = time.time()
    
    print(f"...Pi simulation complete. Total time: {end_time - start_time:.2f} seconds.")

    # Calculate statistics
    mean_dmc, var_dmc, std_dmc = np.mean(estimates_dmc), np.var(estimates_dmc), np.std(estimates_dmc)
    mean_is, var_is, std_is = np.mean(estimates_is), np.var(estimates_is), np.std(estimates_is)
    relative_efficiency = var_dmc / var_is

    print("\n--- Comparison of Pi Estimators ---")
    print(f"{'':<22} | {'Direct MC':<18} | {'Importance Sampling':<20}")
    print(f"-----------------------|--------------------|---------------------")
    print(f"Mean Pi Estimate       | {mean_dmc:<18.6f} | {mean_is:<20.6f}")
    print(f"Variance of Estimate   | {var_dmc:<18.6e} | {var_is:<20.6e}")
    print(f"Std. Dev. of Estimate  | {std_dmc:<18.6e} | {std_is:<20.6e}")
    print(f"-----------------------|--------------------|---------------------")
    print(f"Relative Efficiency    | {'1.0x':<18} | {relative_efficiency:<20.1f}x\n")


# --- Problem 2: Value at Risk (VaR) ---

def monte_carlo_var_dmc(mu, sigma, n_samples, alpha):
    """Monte Carlo estimation of VaR using Direct Sampling."""
    returns = np.random.normal(mu, sigma, n_samples)
    var = np.percentile(returns, 100 * alpha)
    return var

def monte_carlo_var_is(mu_P, sigma_P, mu_Q, sigma_Q, n_samples, alpha):
    """Monte Carlo estimation of VaR using Importance Sampling."""
    # Generate returns from the proposal distribution Q
    returns = np.random.normal(mu_Q, sigma_Q, n_samples)
    
    # Calculate importance weights
    p_val = norm.pdf(returns, loc=mu_P, scale=sigma_P)
    q_val = norm.pdf(returns, loc=mu_Q, scale=sigma_Q)
    weights = p_val / q_val
    
    # Compute weighted percentile for VaR
    # Note: A robust weighted percentile implementation is needed for accuracy.
    # Here we use a simplified approach by sorting and finding the cumulative weight.
    sorted_indices = np.argsort(returns)
    sorted_weights = weights[sorted_indices]
    cumulative_weights = np.cumsum(sorted_weights) / np.sum(weights)
    percentile_index = np.where(cumulative_weights >= alpha)[0][0]
    var = returns[sorted_indices[percentile_index]]

    # Calculate Effective Sample Size (ESS)
    weights_normalized = weights / np.sum(weights)
    ess = 1 / np.sum(weights_normalized**2)
    
    return var, ess

def run_var_comparison(n_runs, n_samples, alpha):
    """Runs and compares DMC and IS for VaR estimation."""
    print("--- 2. Running Value at Risk (VaR) Comparison ---")
    
    # Distribution parameters
    mu_p, sigma_p = 0.001, 0.02  # Target distribution P
    
    # Heuristic for optimal proposal distribution Q
    z_score_alpha = norm.ppf(alpha)
    mu_q = mu_p + z_score_alpha * sigma_p
    sigma_q = sigma_p * 1.5  # Use a wider proposal distribution

    print(f"Running {n_runs} runs of {n_samples} samples each...")
    
    results_dmc = []
    results_is = []
    results_ess = []

    start_time = time.time()
    for _ in range(n_runs):
        # 1. Run Direct MC
        var_dmc = monte_carlo_var_dmc(mu_p, sigma_p, n_samples, alpha)
        results_dmc.append(var_dmc)
        
        # 2. Run Importance Sampling MC
        var_is, ess = monte_carlo_var_is(mu_p, sigma_p, mu_q, sigma_q, n_samples, alpha)
        results_is.append(var_is)
        results_ess.append(ess)
    end_time = time.time()
    
    print(f"...VaR simulation complete. Total time: {end_time - start_time:.2f} seconds.")

    # Calculate statistics
    mean_dmc, var_dmc, std_dmc = np.mean(results_dmc), np.var(results_dmc), np.std(results_dmc)
    mean_is, var_is, std_is = np.mean(results_is), np.var(results_is), np.std(results_is)
    mean_ess = np.mean(results_ess)
    relative_efficiency = var_dmc / var_is

    print("\n--- Comparison of VaR Estimators ---")
    print(f"{'':<22} | {'Direct MC':<18} | {'Importance Sampling':<20}")
    print(f"-----------------------|--------------------|---------------------")
    print(f"Mean VaR Estimate      | {mean_dmc:<18.6f} | {mean_is:<20.6f}")
    print(f"Variance of Estimate   | {var_dmc:<18.6e} | {var_is:<20.6e}")
    print(f"Std. Dev. of Estimate  | {std_dmc:<18.6e} | {std_is:<20.6e}")
    print(f"-----------------------|--------------------|---------------------")
    print(f"Relative Efficiency    | {'1.0x':<18} | {relative_efficiency:<20.1f}x")
    print(f"Avg. Eff. Sample Size  | {'N/A':<18} | {mean_ess:<20.1f} / {n_samples}")

    def plot_results(mu_p, sigma_p, mu_q, sigma_q, alpha, n_plot_samples=500):
        """
        Generates plots to visualize the sampling distributions for both Pi and VaR estimation.
        """
        fig = plt.figure(figsize=(14, 12))
        fig.suptitle('Monte Carlo Method Visualizations', fontsize=16)

        # --- 1. Pi Estimation: Scatter Plot of Samples ---
        ax1 = plt.subplot(2, 2, 1)
        
        # Generate samples for visualization
        samples_dmc_x = [random.uniform(0, 1) for _ in range(n_plot_samples)]
        samples_dmc_y = [random.uniform(0, 1) for _ in range(n_plot_samples)]
        samples_is_x = [1 - sqrt(random.uniform(0, 1)) for _ in range(n_plot_samples)]
        samples_is_y = [1 - sqrt(random.uniform(0, 1)) for _ in range(n_plot_samples)]

        # Plot samples
        ax1.scatter(samples_dmc_x, samples_dmc_y, label='Direct Sampling', alpha=0.6, s=10, color='blue')
        ax1.scatter(samples_is_x, samples_is_y, label='Importance Sampling', alpha=0.6, s=10, color='red')

        # Draw the quarter circle
        circle_x = np.linspace(0, 1, 100)
        circle_y = np.sqrt(1 - circle_x**2)
        ax1.plot(circle_x, circle_y, color='green', linewidth=3, label='Boundary ($x^2+y^2=1$)')

        ax1.set_title('Pi Estimation: Sample Points')
        ax1.set_xlabel('x')
        ax1.set_ylabel('y')
        ax1.set_xlim(0, 1)
        ax1.set_ylim(0, 1)
        ax1.set_aspect('equal', adjustable='box')
        ax1.legend()
        ax1.grid(True, alpha=0.3)

        # --- 2. Pi Estimation: PDF of Importance Sampling ---
        ax2 = plt.subplot(2, 2, 2)
        x = np.linspace(0, 1, 100)
        y = np.linspace(0, 1, 100)
        X, Y = np.meshgrid(x, y)
        
        # PDF of the proposal distribution q(x,y) = 4(1-x)(1-y)
        Z_is = 4 * (1 - X) * (1 - Y)
        # PDF of the direct sampling distribution p(x,y) = 1
        Z_dmc = np.ones_like(X)

        contour = ax2.contourf(X, Y, Z_is, cmap='viridis', levels=15)
        fig.colorbar(contour, ax=ax2, label='Probability Density')
        ax2.plot(circle_x, circle_y, color='white', linestyle='--', linewidth=2, label='Boundary')
        
        ax2.set_title('Pi IS Proposal PDF: $q(x,y)=4(1-x)(1-y)$')
        ax2.set_xlabel('x')
        ax2.set_ylabel('y')
        ax2.set_aspect('equal', adjustable='box')
        ax2.legend()

        # --- 3. VaR Estimation: Probability Density Functions ---
        ax3 = plt.subplot(2, 1, 2)
        x_range = np.linspace(mu_p - 5*sigma_p, mu_p + 5*sigma_p, 1000)
        
        # Plot PDFs
        ax3.plot(x_range, norm.pdf(x_range, loc=mu_p, scale=sigma_p), label='P: Target Distribution', color='blue')
        ax3.plot(x_range, norm.pdf(x_range, loc=mu_q, scale=sigma_q), label='Q: Proposal Distribution', color='red', linestyle='--')
        
        # Add a line for the true VaR
        true_var = norm.ppf(alpha, loc=mu_p, scale=sigma_p)
        ax3.axvline(true_var, color='green', linestyle=':', linewidth=2, label=f'True VaR at {alpha*100:.0f}% ({true_var:.4f})')
        
        # Fill the tail area for the target distribution
        fill_x = np.linspace(mu_p - 5*sigma_p, true_var, 200)
        ax3.fill_between(fill_x, norm.pdf(fill_x, loc=mu_p, scale=sigma_p), color='blue', alpha=0.2, label=f'Target Tail (< VaR)')

        ax3.set_title('VaR Estimation: Probability Density Functions')
        ax3.set_xlabel('Daily Return')
        ax3.set_ylabel('Density')
        ax3.legend()
        ax3.grid(True, alpha=0.3)
        ax3.set_xlim(x_range.min(), x_range.max())

        plt.tight_layout(rect=[0, 0, 1, 0.96])
        plt.show()
    plot_results(mu_p, sigma_p, mu_q, sigma_q, alpha)


def main():
    """Main function to run all comparisons."""
    # --- Configuration ---
    PI_N_SAMPLES = 10_000
    PI_N_RUNS = 100
    
    VAR_N_SAMPLES = 10_000
    VAR_N_RUNS = 1000
    VAR_ALPHA = 0.05

    # Run comparisons
    run_pi_comparison(PI_N_RUNS, PI_N_SAMPLES)
    run_var_comparison(VAR_N_RUNS, VAR_N_SAMPLES, VAR_ALPHA)

if __name__ == "__main__":
    main()
