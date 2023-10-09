#code to demonstrate bar graph
import numpy as np
import matplotlib.pyplot as plt

x = np.array([5, 2, 9, 4, 7])
y = np.array([10, 5, 8, 4, 2])
bar_colors = ['blue', 'yellow', 'red', 'white', 'orange']
plt.bar(x, y, color=bar_colors)

# Add labels to the axes
plt.xlabel('X-axis Label')
plt.ylabel('Y-axis Label')

plt.title('Bar Plot Example')
plt.show()


