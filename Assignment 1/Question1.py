import numpy as np
np.random.seed(22)

size = 250

x1 = np.random.normal(3, 5, size)
x2 = np.random.normal(2, 6, size)
e = np.random.normal(0, 2, size)

y = 3.25 + 1.34 * x1 + 0.8 * x2 + e

print(np.round(y[:15], 2))

print("Minimum value:", np.round(np.min(y), 2))
print("25th percentile:", np.round(np.percentile(y, 25), 2))
print("Median value:", np.round(np.median(y), 2))
print("Mean value:", np.round(np.mean(y), 2))
print("75th percentile:", np.round(np.percentile(y, 75), 2))
print("Maximum value:", np.round(np.max(y), 2))