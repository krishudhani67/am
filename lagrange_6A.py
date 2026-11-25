
import numpy as np
import matplotlib.pyplot as plt

def lagrange_interpolation(x_points, y_points, x_val):

    n = len(x_points)
    result = 0.0
    for i in range(n):
        term = y_points[i]
        for j in range(n):
            if i != j:
                term *= (x_val - x_points[j]) / (x_points[i] - x_points[j])
        result += term
    return result

# Sample data points
x = np.array([1, 2, 3, 4, 5])
y = np.array([2, 4, 1, 3, 7])
x_new = 2.5

y_new = lagrange_interpolation(x, y, x_new)
print(f"Interpolated value at x = {x_new} is y = {y_new:.4f}")

# Build the full interpolating curve and plot it
x_range = np.linspace(min(x), max(x), 200)
y_range = [lagrange_interpolation(x, y, xi) for xi in x_range]

plt.plot(x_range, y_range, "b-")   # Blue interpolation curve
plt.plot(x, y, "ro")               # Red dots for known points
plt.plot(x_new, y_new, "gx")       # Green cross for the estimate
plt.title("Lagrange Interpolation")
plt.show()
