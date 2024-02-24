import matplotlib.pyplot as plt
import numpy as np

# Sample data
arr1 = np.array([1, 2, 3, 4, 5])
arr2 = np.array([5, 4, 3, 2, 1])

# Define colors, sizes, and marker style
colors = ['red', 'green', 'blue', 'orange', 'purple']
sizes = [30, 50, 70, 90, 110]
marker_style = 's'  # 's' stands for square

# Create scatter chart
plt.scatter(arr1, arr2, c=colors, s=sizes, marker=marker_style)

# Customize the plot
plt.xlabel('Array 1')
plt.ylabel('Array 2')
plt.title('Scatter Chart with Different Colors, Sizes, and Square Marker')

# Show the plot
plt.show()
