import numpy as np
np.random.seed(42)

side_effects = np.random.binomial(100, 0.05, 1000)

print(side_effects[:6])
print(np.round(np.mean(side_effects), decimals=1))
print(np.round(np.var(side_effects), decimals=1))