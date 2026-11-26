# ---------------------------------------------------------------
# 5D: Multiple Linear Regression (House Price dataset)
# ---------------------------------------------------------------
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

# Step 1: Create a synthetic but realistic house-price dataset
np.random.seed(42)
n = 120

size = np.random.randint(500, 4000, n)          # square feet
bedrooms = np.random.randint(1, 6, n)
bathrooms = np.random.randint(1, 4, n)
distance = np.random.randint(1, 30, n)           # km from city center

price = (
    3000 * bedrooms
    + 5000 * bathrooms
    + 200 * size
    - 1500 * distance
    + np.random.randint(-10000, 10000, n)        # noise
)

house_data = pd.DataFrame({
    "Size_sqft": size,
    "Bedrooms": bedrooms,
    "Bathrooms": bathrooms,
    "Distance_km": distance,
    "Price": price,
})
print("Sample of the dataset:")
print(house_data.head())

# Step 2: Split into features (X) and target (y), then train/test split
X = house_data[["Size_sqft", "Bedrooms", "Bathrooms", "Distance_km"]]
y = house_data["Price"]
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Step 3: Fit the Multiple Linear Regression model
model = LinearRegression()
model.fit(X_train, y_train)

# Step 4: Predict and evaluate
y_pred = model.predict(X_test)
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print(f"\nCoefficients (beta_1..beta_4): {np.round(model.coef_, 2)}")
print(f"Intercept (beta_0)            : {model.intercept_:.2f}")
print(f"Mean Squared Error (MSE)      : {mse:,.2f}")
print(f"R^2 Score                     : {r2:.4f}")

print("\nFitted regression equation:")
print(f"Price = {model.intercept_:.2f} "
      f"+ ({model.coef_[0]:.2f} * Size_sqft) "
      f"+ ({model.coef_[1]:.2f} * Bedrooms) "
      f"+ ({model.coef_[2]:.2f} * Bathrooms) "
      f"+ ({model.coef_[3]:.2f} * Distance_km)")

# Step 5: Visualize model fit
fig, axes = plt.subplots(1, 2, figsize=(12, 5))

axes[0].scatter(y_test, y_pred, color="steelblue", alpha=0.7)
axes[0].plot([y.min(), y.max()], [y.min(), y.max()], "r--", lw=2)
axes[0].set_xlabel("Actual Price")
axes[0].set_ylabel("Predicted Price")
axes[0].set_title("Actual vs Predicted Price")

residuals = y_test - y_pred
axes[1].scatter(y_pred, residuals, color="seagreen", alpha=0.7)
axes[1].axhline(0, color="red", linestyle="--")
axes[1].set_xlabel("Predicted Price")
axes[1].set_ylabel("Residual (Actual - Predicted)")
axes[1].set_title("Residual Plot")

plt.tight_layout()
plt.show()
