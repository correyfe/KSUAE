import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import LightSource

fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(projection='3d')

x = np.linspace(-5, 5, 100)
y = np.linspace(-5, 5, 100)
X, Y = np.meshgrid(x, y)
Z = (X**2 - Y**2)**2

surf = ax.plot_surface(X, Y, Z, 
                       cmap='viridis',
                       alpha=0.9,
                       linewidth=0,
                       antialiased=True,
                       rstride=2,
                       cstride=2,
                       shade=True)

ax.set_title(r"Поверхность: $z = (x^2 - y^2)^2$",
             fontsize=14, pad=20)
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')

fig.colorbar(surf, ax=ax, shrink=0.5, pad=0.1, label='Значение Z')

plt.show()