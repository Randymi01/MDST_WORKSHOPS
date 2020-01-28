import numpy as np
import matplotlib.pyplot as plt

# Our data...
x = np.linspace(0, 10, 100)
y1, y2, y3 = np.cos(x), np.cos(x + 1), np.cos(x + 2)
names = ['Signal 1', 'Signal 2', 'Signal 3']

fig, (ax1, ax2, ax3) = plt.subplots(3, 1, sharex=True)
ax1.plot(x,y1,'k')
ax1.set_title(names[0])

ax2.plot(x, y2,'k')
ax2.set_title(names[1])

ax3.plot(x, y3,'k')
ax3.set_title(names[2])

plt.setp(plt.gcf().get_axes(), xticks=[], yticks=[])
plt.savefig("Curvey_Curves.png")

plt.show()
