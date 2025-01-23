# Practice: Simulate the heights of 2 million adult women in the United States.
# Google the most recent average height and standard deviation.
# State the standard deviation of the simulated sample in a sentence.
# Use both R and Python.
# Male:
#   Mean: 199.8
#   Standard Error of the Mean: 1.39
#   Number of examined persons: 5085
# Female:
#   Mean: 63.5
#   Standard Error of the Mean: 0.07
#   Number of examined persons: 5,510
import numpy as np

np.random.seed(89)

sample = np.random.normal(loc=63.5, scale= 0.07 * np.sqrt(5510), size=2000000)
rounded_sample = np.round(sample, decimals=1)

for weight in rounded_sample[:6]:
    print(weight)

print(f"Size of sample is {sample.size}")

variance = np.round(np.var(rounded_sample), decimals=1)
mean = np.round(np.mean(rounded_sample), decimals=1)
sd = np.round(np.std(rounded_sample), decimals=1)

print(f"The variance is {variance}")
print(f"The mean is {mean}")
print(f"The standard deviation is {sd}")


