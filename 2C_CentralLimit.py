import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

population = np.random.uniform(0, 1, 100000)
n = 30
samples = np.random.choice(population, size=(1000, n))
means = samples.mean(axis=1)
se = population.std() / np.sqrt(n)

print("Population mean:", round(population.mean(), 4))
print("Population SD:", round(population.std(), 4))
print("Mean of sample means:", round(means.mean(), 4))
print("SD of sample means:", round(means.std(), 4))
print("Theoretical standard error:", round(se, 4))

x = np.linspace(means.min(), means.max(), 200)
plt.hist(means, bins=30, density=True)
plt.plot(x, norm.pdf(x, means.mean(), means.std()), "r-")
plt.title("Central Limit Theorem")
plt.xlabel("Sample mean")
plt.ylabel("Density")
plt.show()
