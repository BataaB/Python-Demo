import numpy as np
np.random.seed(33)

calls = np.random.poisson(1200, 60)
print(np.mean(calls))
print(np.var(calls))