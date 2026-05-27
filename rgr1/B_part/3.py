import numpy as np
import matplotlib.pyplot as plt


fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(projection='3d')

x = np.linspace(-2, 2, 40)
y = np.linspace(-2, 2, 40)
X, Y = np.meshgrid(x, y)
Z = X**2

wire = ax.plot_wireframe(X, Y, Z,
                         cmap='coolwarm',
                         linewidth=0.8, 
                         alpha=0.9,
                         rstride=2,
                         cstride=2)

ax.set_title(r"Каркасная поверхность: $z(x,y) = x^2$, $x, y \in [-2, 2]$",
             fontsize=14, pad=20)
ax.set_xlabel('X(m)')
ax.set_ylabel('Y(m)')
ax.set_zlabel('Z(m)')

mappable = plt.cm.ScalarMappable(cmap='coolwarm')
mappable.set_array(Z)
plt.colorbar(mappable, ax=ax, shrink=0.5, aspect=10)

plt.show()