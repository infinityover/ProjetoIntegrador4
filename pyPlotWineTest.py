import matplotlib.pyplot as plt
import numpy as np

x = np.arange(-2.0, 2, 0.01)
y1 = x**2
y2 = 2

print(y1)

fig, (ax) = plt.subplots(1)
#ax.plot(x, y1, x, y2, color='black')
ax.fill_between(x, y1, y2, where=y2 >= y1, facecolor='darkmagenta', interpolate=True)


#ax.fill_between(x, y1, y2, where=y2 <= y1, facecolor='red', interpolate=True)
ax.set_title('fill between where')

#fig, ax = plt.subplots()
y = np.sin(4*np.pi*x)

#ax.plot(x, y, color='black')
plt.show()
