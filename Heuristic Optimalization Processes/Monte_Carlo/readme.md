# Monte Carlo Simulation: Direct vs. Importance Sampling

This project implements and compares two Monte Carlo (MC) methods: **Direct Monte Carlo (DMC)** and **Importance Sampling (IS)**. The goal is to demonstrate how Importance Sampling can significantly improve the efficiency and reduce the variance of MC estimates, especially when dealing with rare events.

The algorithms are tested on two distinct problems:
1.  Estimating the value of **Pi (π)**.
2.  Calculating **Value at Risk (VaR)** for a financial portfolio.

---

## Implemented Algorithms: Monte Carlo Methods

### 1. Direct Monte Carlo (DMC)
Direct Monte Carlo is the most straightforward simulation method. It involves generating random samples directly from the target distribution (`P`) and averaging the outcomes. While simple to implement, it can be inefficient, requiring a very large number of samples to accurately estimate the probability of rare events.

### 2. Importance Sampling (IS)
Importance Sampling is a variance reduction technique. Instead of sampling from the target distribution `P`, we sample from a different, "proposal" distribution `Q` that is chosen to more frequently generate "important" samples (e.g., samples in the tail of a distribution).

To correct for the change in distribution, each sample is assigned a weight equal to the likelihood ratio `P(x) / Q(x)`. The final estimate is a weighted average. A well-chosen proposal distribution `Q` can dramatically reduce the variance of the estimate, leading to more accurate results with fewer samples.

---

## Showcase Problems

### 1. Estimating the Value of Pi (π)

*   **Problem:** Estimate the value of π by calculating the area of a unit circle. We simulate random points in a square and determine the ratio of points that fall inside the inscribed circle.
*   **Implementations:**
    *   `piSImulationDMC.py`: Uses Direct MC, sampling points uniformly across the square.
    *   `piSimulationIS.py`: Uses Importance Sampling, with a proposal distribution that concentrates samples in more "interesting" areas.
*   **Evaluation:** The algorithms are compared based on the variance of their π estimates over multiple runs. A lower variance indicates a more stable and reliable estimator.

### 2. Calculating Value at Risk (VaR)

*   **Problem:** VaR is a financial metric that estimates the maximum potential loss of a portfolio over a specific time frame for a given confidence level (e.g., 95%). Calculating VaR involves estimating the value of a low percentile (e.g., the 5th percentile) of the portfolio's return distribution, which is a rare event.
*   **Implementation:**
    *   `ValueAtRisk.py`: Implements and compares both DMC and IS for VaR estimation.
        *   **Direct MC (`monte_carlo_var`)**: Simulates returns from the target distribution `P` and finds the 5th percentile.
        *   **Importance Sampling (`monte_carlo_var_IS`)**: Simulates returns from a proposal distribution `Q` whose mean is shifted towards the loss region (the tail). This generates more relevant samples for estimating extreme losses.
*   **Evaluation:** The key metric is the **variance of the VaR estimator** over many runs. The script also calculates the **Relative Efficiency** (`variance_DMC / variance_IS`) to quantify the performance gain and the **Effective Sample Size (ESS)** to measure the quality of the weighted sample.

---

## How to Run

### Prerequisites
You need Python 3 and the following libraries installed:
```bash
pip install numpy matplotlib scipy
```

### Execution
To run the simulations, execute the scripts from your terminal:

**Pi Estimation:**
```bash
# Run Direct Monte Carlo for Pi
python "g:\My Drive\HOP\Monte Carlo\piSImulationDMC.py"

# Run Importance Sampling for Pi
python "g:\My Drive\HOP\Monte Carlo\piSimulationIS.py"
```

**Value at Risk (VaR) Comparison:**
```bash
# Run the VaR comparison script
python "g:\My Drive\HOP\Monte Carlo\ValueAtRisk.py"
```

---

## Experiments and Results

The experiments consist of running each simulation multiple times (`N_RUNS`) with a fixed number of samples per run (`N_SAMPLES_PER_RUN`) to analyze the stability and variance of the estimators.

### Value at Risk (VaR) Results

The `ValueAtRisk.py` script produces a detailed comparison. The results clearly show that Importance Sampling yields a much more stable estimate (lower variance) than Direct MC.

**Example Output:**
```
Running comparison: 1000 runs of 10000 samples each...
...Simulation complete. Total time: 11.54 seconds.

--- Comparison of VaR Estimators ---
                     | Direct MC            | Importance Sampling
---------------------|----------------------|---------------------
Mean VaR Estimate    | -0.031958            | -0.031945
Variance of Estimate | 2.156941e-07         | 1.348623e-08
Std. Dev. of Estimate| 4.644287e-04         | 1.161302e-04
---------------------|----------------------|---------------------
Relative Efficiency  | 1.0x                 | 16.0x
Avg. Eff. Sample Size| N/A                  | 1854.2 / 10000
```

| Metric | Direct MC | Importance Sampling |
| :--- | :--- | :--- |
| **Mean VaR Estimate** | -0.031958 | -0.031945 |
| **Variance of Estimate** | 2.16e-07 | **1.35e-08** |
| **Relative Efficiency** | 1.0x | **16.0x** |

### Conclusion

In both test problems, the **Importance Sampling (IS)** method produced estimates with significantly lower variance than **Direct Monte Carlo (DMC)** using the same number of samples. For the VaR problem, IS was approximately **16 times more efficient**.

This demonstrates that Importance Sampling is a powerful heuristic technique for improving the efficiency of simulations, particularly for problems involving the estimation of rare or extreme events.