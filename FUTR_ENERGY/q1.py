import matplotlib.pyplot as plt
import numpy as np

# Defining our  lines and polygons
lines = [np.array([[1, 2], [3, 4]]), np.array([[5, 6], [7, 8]])]
polygons = [np.array([[1, 2], [3, 4], [5, 6]]), np.array([[7, 8], [9, 10], [11, 12], [13, 14]])]

# Defining labels for lines and polygons
line_labels = ['Line 1', 'Line 2']
polygon_labels = ['Polygon 1', 'Polygon 2']

# Defining any two random points
red_point = np.array([2, 3])
green_point = np.array([10, 11])

# Plotting lines
for line, label in zip(lines, line_labels):
    plt.plot(line[:, 0], line[:, 1], label=label)

# Plotting polygons
for polygon, label in zip(polygons, polygon_labels):
    plt.plot(polygon[:, 0], polygon[:, 1], label=label)

# Plotting random points
plt.scatter(*red_point, color='red', label='Red Point')
plt.scatter(*green_point, color='green', label='Green Point')

# Adding labels
for i, point in enumerate(lines[0]):
    plt.text(point[0], point[1], f'{i+1}', fontsize=12, ha='right')
for i, point in enumerate(polygons[0]):
    plt.text(point[0], point[1], f'{i+1}', fontsize=12, ha='right')

plt.legend()
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Lines, Polygons, and Random Points')
plt.grid(True)
plt.show()
