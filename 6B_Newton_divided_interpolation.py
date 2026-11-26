import numpy as np
import matplotlib.pyplot as plt

def divided_diff(x, y):
    n = len(y)
    table = [[0.0] * n for _ in range(n)]

    for i in range(n):
        table[i][0] = y[i]

    for j in range(1, n):
        for i in range(n - j):
            table[i][j] = (table[i + 1][j - 1] - table[i][j - 1]) / (x[i + j] - x[i])

    return table

def newton_interpolation(x, y, value):
    table = divided_diff(x, y)
    result = table[0][0]
    product_term = 1.0

    for i in range(1, len(x)):
        product_term *= value - x[i - 1]
        result += table[0][i] * product_term

    return result

x_points = [1, 2, 3, 4]
y_points = [1, 4, 9, 16]

table = divided_diff(x_points, y_points)
print("Divided-difference table:")
for row in table:
    print(["%.4f" % v for v in row])

value_to_interpolate = 2.5
interpolated_value = newton_interpolation(x_points, y_points, value_to_interpolate)
print(f"Interpolated value at x = {value_to_interpolate} is {interpolated_value:.4f}")

x_range = np.linspace(min(x_points), max(x_points), 200)
y_range = [newton_interpolation(x_points, y_points, xi) for xi in x_range]

plt.figure(figsize=(8, 5))
plt.plot(x_range, y_range, color="purple", label="Newton interpolation curve")
plt.scatter(x_points, y_points, color="red", zorder=5, label="Known data points")
plt.scatter(value_to_interpolate, interpolated_value, color="green", marker="x",
            s=100, zorder=5, label="Interpolated point")
plt.title("Newton's Divided-Difference Interpolation")
plt.xlabel("x")
plt.ylabel("y")
plt.legend()
plt.grid(alpha=0.3)
plt.show()
