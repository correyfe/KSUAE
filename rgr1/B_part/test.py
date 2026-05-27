import matplotlib.pyplot as plt
import numpy as np

# 1. Создаем вектор параметра t (например, от -2 до 2)
t = np.linspace(-2, 2, 200)

# 2. Задаем кубические параметрические уравнения
x = t
y = t**2
z = t**3

# 3. Инициализируем 3D-график
fig = plt.figure(figsize=(10, 7))
ax = fig.add_subplot(111, projection='3d')

# 4. Строим кривую
ax.plot(x, y, z, label='Кубическая кривая ($t, t^2, t^3$)', color='blue', linewidth=2.5)

# 5. Настраиваем подписи осей и заголовок
ax.set_xlabel('Ось X')
ax.set_ylabel('Ось Y')
ax.set_zlabel('Ось Z')
ax.set_title('Пространственная кубическая кривая в 3D', fontsize=14)

# 6. Добавляем сетку и легенду
ax.grid(True)
ax.legend()

# 7. Отображаем график
plt.show()
