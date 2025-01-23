import numpy as np
from scipy.stats import truncnorm
# from scipy import stats as st
np.random.seed(42)
# Define the parameters
lower_bound = 4
upper_bound = 17
mean = 9
std_dev = 3
# Calculate the a and b parameters for truncnorm
a = (lower_bound - mean) / std_dev
b = (upper_bound - mean) / std_dev
# Generate random samples
ages = np.round(truncnorm.rvs(a, b, loc=mean, scale=std_dev,size=50))
# import numpy as np
import matplotlib.pyplot as plt
# Create the boxplot
plt.boxplot(ages)
plt.title("Boxplot of Ages")
plt.xlabel("Group")
plt.ylabel("Age")
plt.show()