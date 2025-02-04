import numpy as np
from scipy.stats import truncnorm
from scipy import stats as st
np.random.seed(42)
# Define the parameters
lower_bound = 200
upper_bound = 800
mean = 527
std_dev = 112
# Calculate the a and b parameters for truncnorm
a = (lower_bound - mean) / std_dev
b = (upper_bound - mean) / std_dev
# Generate random samples
GMATSc = np.round(truncnorm.rvs(a, b, loc=mean,
scale=std_dev, size=10000))
print(GMATSc[:6])

print("Minimum:", np.round(np.min(GMATSc), 1))
print("1st Qu:", np.round(np.percentile(GMATSc, 25), 1))
print("Median:", np.round(np.median(GMATSc), 1))
print("Mean:", np.round(np.mean(GMATSc), 1))
print("3rd Qu:", np.round(np.percentile(GMATSc, 75), 1))
print("Maximum:", np.round(np.max(GMATSc), 1))

#Standard Deviation
std_dev = np.std(GMATSc)
print("Standard Deviation:", np.round(np.std(GMATSc)))

#Density Plot
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
sns.kdeplot(GMATSc)
plt.title('Density Plot of GMAT Scores')
plt.xlabel('GMAT Score')
plt.ylabel('Density')
plt.show()

# Create the histogram
plt.hist(GMATSc, bins=12)
# Add labels and title
plt.xlabel('GMAT Scores')
plt.ylabel('Frequency')
plt.title('Histogram of GMAT Scores')
# Show the plot
plt.show()

import numpy as np
import matplotlib.pyplot as plt
# Create the boxplot
plt.boxplot(GMATSc)
plt.title("Boxplot of GMAT Scores")
plt.xlabel("Group")
plt.ylabel("GMAT Score")
plt.show()

import numpy as np
from scipy.stats import truncnorm
np.random.seed(42)
# Define the parameters
lower_bound = 200
upper_bound = 800
mean = 527
std_dev = 112
# Calculate the a and b parameters for truncnorm
a = (lower_bound - mean) / std_dev
b = (upper_bound - mean) / std_dev
# Generate random samples
GMATSc = np.round(truncnorm.rvs(a, b, loc=mean,
scale=std_dev, size=10000))
# Calculate quantiles
q1 = np.percentile(GMATSc, 25)
q3 = np.percentile(GMATSc, 75)
iqr = q3 - q1
# Calculate upper and lower bounds
upper_bound = q3 + 1.5 * iqr
lower_bound = q1 - 1.5 * iqr
# Identify outliers
outliers = [x for x in GMATSc if x < lower_bound or x >
upper_bound]
print(np.round(outliers))

#CI for the mean
import numpy as np
import scipy.stats as stats
from scipy.stats import truncnorm
np.random.seed(42)
# Define the parameters
lower_bound = 200
upper_bound = 800
mean = 527
std_dev = 112
# Calculate the a and b parameters for truncnorm
a = (lower_bound - mean) / std_dev
b = (upper_bound - mean) / std_dev
# Generate random samples
GMATSc = np.round(truncnorm.rvs(a, b, loc=mean,
scale=std_dev, size=10000))
# Calculate the sample mean and standard deviation
sample_mean = np.mean(GMATSc)
sample_std = np.std(GMATSc, ddof=1) # Use ddof=1 for unbiased estimator
# Set the confidence level
confidence_level = 0.95
# Calculate the critical value (t-statistic)
t_crit = stats.t.ppf((1 + confidence_level) / 2,
df=len(GMATSc) - 1)
# Calculate the margin of error
margin_of_error = t_crit * sample_std / np.sqrt(len(GMATSc))
# Calculate the confidence interval
confidence_interval = (sample_mean - margin_of_error,
sample_mean + margin_of_error)
print(confidence_interval)