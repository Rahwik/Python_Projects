import numpy as np
import matplotlib.pyplot as plt

y = np.array([8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18])
y1 = np.array([18, 19, 1, 7, 12, 3, 4, 5, 6, 7, 11])
plt.plot(y, marker='*', ms=20, mec='b', mfc='b', linestyle='dashed', color='red', linewidth=2)
plt.plot(y1)
plt.xlabel('x-axis')
plt.ylabel('y-axis')
plt.title("Square Numbers")
plt.suptitle('Square')
plt.grid(axis='y', linestyle='dotted', color='pink', linewidth=10)

plt.show()
