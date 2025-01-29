import numpy as np
from scipy.stats import truncnorm
import matplotlib.pyplot as plt
# from scipy import stats as st
import statistics as st

np.random.seed(22)

small = 15
large = 49
mean = 29
std = 2.5
size = 1000000

a = (small - mean) / std
b = (large - mean) / std

ages = np.round(truncnorm.rvs(a, b, loc=mean, scale=std, size=size))

print("Mode:", np.round(st.mode(ages), decimals=2))
print("Variation:", np.round(st.variance(ages), decimals=2))
print("Standard Deviation:", np.round(st.stdev(ages), decimals=2))
print("Minimum value:", np.round(np.min(ages), 2))
print("25th percentile:", np.round(np.percentile(ages, 25), 2))
print("Median value:", np.round(np.median(ages), 2))
print("Mean value:", np.round(np.mean(ages), 2))
print("75th percentile:", np.round(np.percentile(ages, 75), 2))
print("Maximum value:", np.round(np.max(ages), 2))

plt.boxplot(ages)
plt.title("Boxplot of Ages")
plt.xlabel("Group")
plt.ylabel("Age")
plt.show()