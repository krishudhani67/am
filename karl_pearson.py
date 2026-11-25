# ---------------------------------------------------------------
# 5A: Karl Pearson's Coefficient of Correlation
# ---------------------------------------------------------------
import numpy as np
import matplotlib.pyplot as plt
def pearson_correlation(x, y):
    
    x = np.asarray(x, dtype=float)
    y = np.asarray(y, dtype=float)
    x_mean, y_mean = x.mean(), y.mean()

    numerator = np.sum((x - x_mean) * (y - y_mean))
    denominator = np.sqrt(np.sum((x - x_mean) ** 2)) * np.sqrt(np.sum((y - y_mean) ** 2))
    return numerator / denominator

# Example: hours studied vs marks obtained
hours_studied = [2, 4, 6, 8, 10, 3, 7, 5, 9, 1]
marks_obtained = [50, 60, 68, 82, 90, 55, 75, 65, 88, 40]

r_manual = pearson_correlation(hours_studied, marks_obtained)
r_numpy = np.corrcoef(hours_studied, marks_obtained)[0, 1]   # built-in cross-check

print(f"Pearson correlation coefficient (from scratch) : {r_manual:.4f}")
print(f"Pearson correlation coefficient (numpy check)  : {r_numpy:.4f}")

if r_manual > 0.7:
    strength = "strong positive"
elif r_manual > 0.3:
    strength = "moderate positive"
elif r_manual > -0.3:
    strength = "weak/no linear"
elif r_manual > -0.7:
    strength = "moderate negative"
else:
    strength = "strong negative"
print(f"Interpretation: a {strength} linear relationship between hours studied and marks.")

m, c = np.polyfit(hours_studied, marks_obtained, 1)
x = np.array([min(hours_studied), max(hours_studied)])

plt.scatter(hours_studied, marks_obtained)
plt.plot(x, m*x + c, "r--")
plt.xlabel("Hours studied")
plt.ylabel("Marks obtained")
plt.show()
