# ---------------------------------------------------------------
# 6B: Newton's Divided-Difference Interpolation Method
# ---------------------------------------------------------------
import numpy as np
import matplotlib.pyplot as plt

def divided_diff(x, y):
    """Build the divided-difference table. Returns the full n x n table."""
    n = len(y)
    table = [[0.0] * n for _ in range(n)]
    for i in range(n):
        table[i][0] = y[i]
    for j in range(1, n):   #j=1, 2, 3
        for i in range(n - j):  #0,1,2
            table[i][j] = (table[i + 1][j - 1] - table[i][j - 1]) / (x[i + j] - x[i])
    return table

print(table)

def newton_interpolation(x, y, value):
    """Estimate y at 'value' using Newton's divided-difference formula."""
    n = len(x)
    table = divided_diff(x, y)
    result = table[0][0]
    product_term = 1.0
    for i in range(1, n):
        product_term *= (value - x[i - 1])
        result += table[0][i] * product_term
    return result

# Example: f(x) = x^2, so interpolation should recover x^2 exactly (it's a degree-2 fit)
x_points = [1, 2, 3, 4]
y_points = [1, 4, 9, 16]     # x^2

# Show the divided-difference table for reference
table = divided_diff(x_points, y_points)
print("Divided-difference table (row i, column j = f[x_i,...,x_{i+j}]):")
for row in table:
    print(["%.4f" % v for v in row])

value_to_interpolate = 2.5
interpolated_value = newton_interpolation(x_points, y_points, value_to_interpolate)
print(f"\nInterpolated value at x = {value_to_interpolate} is {interpolated_value:.4f}")
print("(Exact x^2 value would be 6.25 - matches, since the data is exactly quadratic.)")

# Plot the interpolating curve
x_range = np.linspace(min(x_points), max(x_points), 200)
y_range = [newton_interpolation(x_points, y_points, xi) for xi in x_range]

plt.figure(figsize=(8, 5))
plt.scatter(x_points, y_points, color="red", zorder=5, label="Known data points")
plt.plot(x_range, y_range, color="purple", label="Newton interpolation curve")
plt.scatter([value_to_interpolate], [interpolated_value], color="green", marker="x",
            s=100, zorder=5, label=f"Interpolated point (x={value_to_interpolate})")
plt.title("Newton's Divided-Difference Interpolation")
plt.xlabel("x")
plt.ylabel("y")
plt.legend()
plt.grid(alpha=0.3)
plt.show()
