import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Задание 1. График (Кубическая кривая)
# x(t) = t
# y(t) = t^2
# z(t) = t^3
# t от -2 до 2

fig1 = plt.figure(figsize=(10, 8))
ax1 = fig1.add_subplot(111, projection='3d')

# создаю параметр t
t_value = []
for i in range(-100, 101):
    t_value.append(i / 50.0)
t_value = np.array(t_value)

# вычисляю координаты
x_coord = t_value
y_coord = t_value ** 2
z_coord = t_value ** 3

# рисую линию
ax1.plot(x_coord, y_coord, z_coord, linewidth=2, color='blue', linestyle='-')

# добавляю маркеры в ключевых точках
marker_points = [0, 50, 100, 150, 200]
for idx in marker_points:
    ax1.scatter(x_coord[idx], y_coord[idx], z_coord[idx], color='red', s=80)

ax1.set_xlabel('x')
ax1.set_ylabel('y')
ax1.set_zlabel('z')
ax1.set_title('Кубическая кривая: x=t, y=t^2, z=t^3')
ax1.grid()

# Задание 2. Точечный график (Значения многочленов)
# z = i^3 - 3*i^2*j + 2*i*j^2
# i, j от -3 до 3

fig2 = plt.figure(figsize=(10, 8))
ax2 = fig2.add_subplot(111, projection='3d')

i_list = [-3, -2, -1, 0, 1, 2, 3]
j_list = [-3, -2, -1, 0, 1, 2, 3]

i_all = []
j_all = []
z_all = []

for i_val in i_list:
    for j_val in j_list:
        i_all.append(i_val)
        j_all.append(j_val)
        z_result = i_val**3 - 3*i_val**2*j_val + 2*i_val*j_val**2
        z_all.append(z_result)

i_arr = np.array(i_all)
j_arr = np.array(j_all)
z_arr = np.array(z_all)

# рисую точки с цветовой кодировкой по z
scatter_plot = ax2.scatter(i_arr, j_arr, z_arr, c=z_arr, cmap='viridis', s=100, marker='^', alpha=0.8)

ax2.set_xlabel('i')
ax2.set_ylabel('j')
ax2.set_zlabel('z')
ax2.set_title('Многочлены: z = i^3 - 3*i^2*j + 2*i*j^2')

plt.colorbar(scatter_plot, ax=ax2)
ax2.grid()


# Задание 3. Каркасная поверхность (Параболический цилиндр)
# z = x^2
# x, y от -2 до 2

fig3 = plt.figure(figsize=(10, 8))
ax3 = fig3.add_subplot(111, projection='3d')

# создаю сетку для x и y
x_vals = np.linspace(-2, 2, 30)
y_vals = np.linspace(-2, 2, 30)

X_mesh, Y_mesh = np.meshgrid(x_vals, y_vals)
Z_mesh = X_mesh ** 2

# рисую каркас
ax3.plot_wireframe(X_mesh, Y_mesh, Z_mesh, color='blue', alpha=0.7)

ax3.set_xlabel('x')
ax3.set_ylabel('y')
ax3.set_zlabel('z')
ax3.set_title('Параболический цилиндр: z = x^2')
ax3.grid()


# Задание 4. Сплошная поверхность (Поверхность четвёртой степени)
# z = x^4 - 2*x^2*y^2 + y^4
# x, y от -1 до 1

fig4 = plt.figure(figsize=(10, 8))
ax4 = fig4.add_subplot(111, projection='3d')

x_s = np.linspace(-1, 1, 40)
y_s = np.linspace(-1, 1, 40)

X_s, Y_s = np.meshgrid(x_s, y_s)
Z_s = X_s**4 - 2*X_s**2*Y_s**2 + Y_s**4

# рисую сплошную поверхность
surf = ax4.plot_surface(X_s, Y_s, Z_s, cmap='coolwarm', alpha=0.9, shade=True)

ax4.set_xlabel('x')
ax4.set_ylabel('y')
ax4.set_zlabel('z')
ax4.set_title('Поверхность четвёртой степени: z = x^4 - 2*x^2*y^2 + y^4')

cbar = plt.colorbar(surf, ax=ax4)
cbar.set_label('Высота')
ax4.grid()


# Задание 5. Комбинированный график
# Сочетание: поверхность + касательная плоскость + линия пересечения

fig5 = plt.figure(figsize=(12, 9))
ax5 = fig5.add_subplot(111, projection='3d')

# рисую основную поверхность z = x^4 - 2*x^2*y^2 + y^4
x_c = np.linspace(-1, 1, 35)
y_c = np.linspace(-1, 1, 35)
X_c, Y_c = np.meshgrid(x_c, y_c)
Z_c = X_c**4 - 2*X_c**2*Y_c**2 + Y_c**4

surf_main = ax5.plot_surface(X_c, Y_c, Z_c, cmap='plasma', alpha=0.7)

# добавляю касательную плоскость (в точке 0,0 это z=0)
x_plane = np.linspace(-1, 1, 15)
y_plane = np.linspace(-1, 1, 15)
X_plane, Y_plane = np.meshgrid(x_plane, y_plane)
Z_plane = np.zeros_like(X_plane)

ax5.plot_surface(X_plane, Y_plane, Z_plane, color='yellow', alpha=0.3)

# добавляю точку экстремума
ax5.scatter([0], [0], [0], color='red', s=200, marker='*')

# добавляю кривую - пересечение с плоскостью y=x
t_line = np.linspace(-1, 1, 50)
x_line = t_line
y_line = t_line
z_line = t_line**4 - 2*t_line**2*t_line**2 + t_line**4
z_line = 2 * t_line**4

ax5.plot(x_line, y_line, z_line, 'g-', linewidth=3)

ax5.set_xlabel('x')
ax5.set_ylabel('y')
ax5.set_zlabel('z')
ax5.set_title('Комбинированный график')
ax5.grid()

cbar5 = plt.colorbar(surf_main, ax=ax5)
cbar5.set_label('Высота')

# показываю все графики
plt.show()
