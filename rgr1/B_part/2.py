import numpy as np
import matplotlib.pyplot as plt


fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(projection='3d')

i_vals = np.arange(-3, 4)
j_vals = np.arange(-3, 4)

I, J = np.meshgrid(i_vals, j_vals)
Z = I**3 - 3*(I**2)*J + 2*I*(J**2)

I = I.flatten()
J = J.flatten()
Z = Z.flatten()

scatter = ax.scatter(I, J, Z, 
                     c=Z,
                     s=30,
                     cmap='viridis',
                     alpha=0.7,
                     marker='p')

ax.set_xlabel('I')
ax.set_ylabel('J')
ax.set_zlabel('Z')

ax.set_title(r'Точечный график: $z_{ij} = i^3 - 3i^2j + 2ij^2, \ i,j \in [-3, 3]$', 
             fontsize=14, pad=20)

ax.grid(True)
plt.show()
