import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm
from matplotlib.ticker import LinearLocator
from matplotlib.colors import LightSource

fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(projection='3d')

x = np.linspace(-5, 5, 100)
y = np.linspace(-5, 5, 100)
X, Y = np.meshgrid(x, y)
Z1 = (X**2 - Y**2)**2
Z2 = np.zeros_like(X)

ls = LightSource(azdeg=225, altdeg=45)
rgb = ls.shade(Z1, cmap=cm.coolwarm, 
                vert_exag=0.1, 
                blend_mode='soft')

surf1 = ax.plot_surface(X, Y, Z1, 
                       facecolors=rgb,
                       linewidth=0,
                       antialiased=False,
                       alpha=0.9)

surf2 = ax.plot_surface(X, Y, Z2,
                        cmap=cm.viridis,
                        alpha=0.7,
                        linewidth=0.1,
                        edgecolors='black',)

ax.set_title("Комбинированный график: ")
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.zaxis.set_major_locator(LinearLocator(10))

info_text = """Этот график демонстрирует поверхность, определённую функцией $z = (x^2 - y^2)^2$,
а также касательную плоскость в ее точке экстремума.
Цвет показывает значение параметра Z"""

ax.text2D(0.05, 0, info_text, transform=ax.transAxes, 
          fontsize=8,
          verticalalignment='bottom',
          bbox=dict(boxstyle='round', facecolor='wheat', 
          alpha=0.8))

plt.show()