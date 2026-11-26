# 3D: F-test for Comparison of Variances

import numpy as np
from scipy.stats import f

# Two samples
A = [10.2, 9.8, 10.5, 10.1, 9.9, 10.3, 10.0]
B = [9.5, 10.6, 9.2, 10.8, 9.4, 10.9, 9.1]

# Calculate variances
var_A = np.var(A, ddof=1)
var_B = np.var(B, ddof=1)

# Put larger variance in numerator
if var_A > var_B:
    F = var_A / var_B
    df1 = len(A) - 1
    df2 = len(B) - 1
else:
    F = var_B / var_A
    df1 = len(B) - 1
    df2 = len(A) - 1

# Significance level
alpha = 0.05

# Critical value
F_critical = f.ppf(1 - alpha / 2, df1, df2)

# Print results
print("Variance A:", round(var_A, 4))
print("Variance B:", round(var_B, 4))
print("F value:", round(F, 4))
print("Critical F:", round(F_critical, 4))

# Decision
if F > F_critical:
    print("Reject H0: Variances are significantly different")
else:
    print("Fail to Reject H0: Variances are not significantly different")
