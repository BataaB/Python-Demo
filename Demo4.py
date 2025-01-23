import numpy as np

np.random.seed(100)

sample = np.random.normal(loc=199, scale=25, size=1000000)

rounded_sample = np.round(sample, decimals=1)

for weight in rounded_sample[:6]:
    print(weight)

variance = np.round(np.var(rounded_sample), decimals=1)
mean = np.round(np.mean(rounded_sample), decimals=1)
sd = np.round(np.std(rounded_sample), decimals=1)

print(f"The variance is {variance}")
print(f"The mean is {mean}")
print(f"The standard deviation is {sd}")