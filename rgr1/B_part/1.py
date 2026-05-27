import numpy as np
import matplotlib.pyplot as plt


fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(projection='3d')

t = np.linspace(0, 10, 50)
x = t
y = t**2
z = t**3

ax.plot(x, y, z,
        alpha=0.5,
        linewidth=1.5, 
        color='blue', 
        linestyle='-')

ax.scatter(x, y, z, c=z,
           cmap='viridis', 
           s=30)

ax.set_title(r'Кубическая кривая: $\left\{x=t, \ y=t^2, \ z=t^3\right\}, \ t \in [0, 10]$', 
             fontsize=14, pad=20)
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')

plt.show()
