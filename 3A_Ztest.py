# 3A: Large Sample Z-test for a Single Mean

import numpy as np
from scipy.stats import norm

# Sample data
sample = np.random.normal(50.6, 2, 40)

# Given values
mu = 50 # Hypothesized mean
alpha = 0.05 # Significance level
n = len(sample) # Sample size

# Calculate sample mean
x_bar = np.mean(sample)

# Calculate sample standard deviation
sigma = np.std(sample, ddof=1)

# Calculate Z value
z = (x_bar - mu) / (sigma / np.sqrt(n))

# Calculate p-value (two-tailed test)
p_value = 2 * (1 - norm.cdf(abs(z)))

# Print results
print("Sample Mean:", round(x_bar, 4))
print("Z value:", round(z, 4))
print("P-value:", round(p_value, 4))

# Decision
if p_value < alpha:
    print("Reject H0")
else:
    print("Fail to Reject H0")
