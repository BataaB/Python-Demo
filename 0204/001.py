import numpy as np
import matplotlib.pyplot as plt
np.random.seed(25)
# Set the scale parameter (inverse of the rate parameter)
scale = 0.5
# Generate 1000 samples from the exponential distribution
samples = np.random.exponential(scale=scale, size=1000)
# You can now analyze the generated samples
print(samples[:6])


print("Mean:", np.round(np.mean(samples), 2))


# Generate random samples from exponential distribution
scale = 0.5 # Scale parameter (mean = 1/scale)
size = 1000 # Number of samples
samples = np.random.exponential(scale, size)
# Plot the theoretical exponential distribution
x = np.linspace(0, max(samples), 100)
y = (1/scale) * np.exp(-x/scale)
plt.plot(x, y, 'r-', label='Theoretical Distribution')
plt.title('Exponential Distribution')
plt.xlabel('x')
plt.ylabel('Density')
plt.legend()
plt.show()




# Generate random samples from exponential distribution
scale = 0.5 # Scale parameter (mean = 1/scale)
size = 1000 # Number of samples
samples = np.random.exponential(scale, size)
def count_values_less_than(data, value):
    """Counts the number of values in a given data
    structure that are less than a given value."""
    count = 0
    for item in data:
        if item < value:
            count += 1
    return count
numbers = samples
target_value = 1
result = count_values_less_than(numbers, target_value)
prob=result/len(samples)
print(prob)