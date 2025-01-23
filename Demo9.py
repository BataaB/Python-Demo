import matplotlib.pyplot as plt
import pandas as pd

# Sample data
data = pd.read_excel(r"airqualityData.xlsx")
x = data['Wind']
y = data['Temp']

# Create the scatter plot
plt.scatter(x, y)

# Add labels and title
plt.xlabel('Wind')
plt.ylabel('Temperature')
plt.title('Wind vs Temperature')

# Display the plot
plt.show()