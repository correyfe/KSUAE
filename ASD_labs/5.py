# 1
# a=[[1,2,3],[4,5,6],[7,8,9]]
# print(a)
# b=a.copy()
# print(b)
# print(id(a),id(b),id([[1,2,3],[4,5,6],[7,8,9]]))
# 2
# a=3
# mas=[0]*3
# for i in range(a):
#     mas[i]=[0]*3
#     print(mas[i])
# print(mas)
# 3
# mas=[]
# n=int(input('введите размер n= '))
# mas=[0 for i in range(n)]
# print(mas)
# 4
# n=int(input('введите размер n= '))
# mas=[0]*n
# for i in range(n):
#     mas[i]=4
# print(mas)
# 6
# print('двумерный массив a[n][m]. Количество элементов nxm')
# n = int(input('n = '))
# m = int(input('m = '))
# mas = [[ 0 for i in range(m)] for j in range(n)]
# print(mas)
# 7
# n = int(input('n = '))
# m = int(input ('m = '))
# mas = [[0 for i in range(m)] for j in range(n)]
# for i in range(n): 
#     for j in range(m): 
#         mas [1][j]=10
# print (mas)
# print()
# 8
# n = int(input('n = '))
# m = int(input('m = '))
# mas = [[0 for i in range (m)] for j in range(n)]
# for i in range(n): 
#     for j in range(m):
#          mas [1][j]=7
#          print (mas[i][j], end = ' ')
#     print ()
# print()
# 9
# from random import randint
# n = int(input('n = '))
# m = int(input('m = '))
# mas = [[0 for i in range(m)] for j in range(n)]
# for i in range(n):
#     for j in range(m):
#         mas[i][j] = randint(10, 99)

# for i in range(n):
#     for j in range(m):
#         print(mas[i][j], end=' ')
#     print()
# print()
# 11
# from random import randint
# n=int(input())
# m=int(input())
# mas=[[0 for i in range(m)] for j in range(n)]
# for i in range(n):
#     for j in range(m):
#         mas[i][j]=randint(10,99)

# s=0
# for i in range(n):
#     for j in range(m):
#         s+=mas[i][j]
# print(s)
# 12
# from random import randint
# n = int(input('n = '))
# m = int(input('m = '))

# mas = [[0 for i in range(m)] for j in range(n)]
# for i in range(n):
#     for j in range(m):
#         mas[i][j] = randint(10, 99)

# for i in range(n):
#     for j in range(m):
#         print(mas[i][j], end=' ')
#     print()

# for i in range(n):
#     for j in range(m):
#         if mas[i][j] % 2 == 0:
#             mas[i][j] = 10

# print()
# for i in range(n):
#     for j in range(m):
#         print(mas[i][j], end=' ')
#     print()
# 13
# A = [1, 5, 8, 100, 200, 2000]
# x = 200
# i = 0
# while A[i] != x:
#     i += 1
# print("A[", i, "]=", x, sep="")
# 14
# from random import randint
# A = []
# N = int(input('Введите размер N = '))
# A = [0 for i in range(N)]

# for i in range(N):
#     A[i] = randint(90, 100)
# print(A)

# i = 0
# X = 95
# while i < N and A[i] != X:
#     i += 1
#     if i < N:
#         print("A[", i, "]=", X, sep="")
#     else:
#         print("Не нашли!")
# 15
# from random import randint
# A = []
# N = int(input('Введите размер N = '))
# A = [0 for i in range(N)]
# X = 95

# for i in range(N):
#     A[i] = randint(90, 100)
# print(A)

# for i in range(len(A)):
#     if A[i] == X:
#         print("A[", i, "]=", X, sep="")
#         break
# else:
#     print("Не нашли!")
# 16
# from random import randint
# A = []
# N = int(input('Введите размер N = '))
# A = [0 for i in range(N)]

# for i in range(N):
#     A[i] = randint(1, 100)
# print(A)

# M = A[0]
# for i in range(1, N):
#     if A[i] > M:
#         M = A[i]
# print(M)

# ГРАФИКИ
import matplotlib.pyplot as plt
import numpy as np

# Различные способы построения графиков
fig, axes = plt.subplots(2, 2, figsize=(12, 8))

x = np.linspace(0, 5, 50)

# 1. Линейный график
axes[0, 0].plot(x, x**2, label='x^2')
axes[0, 0].plot(x, x**3, label='x^3')
axes[0, 0].set_title('Криволинейные графики')
axes[0, 0].legend()

# 2. Точечный график
noise = np.random.normal(0, 1, 50)
axes[0, 1].scatter(x, x**2 + noise, alpha=0.6, c='red', s=50)
axes[0, 1].set_title('Точечный график')

# 3. Ступенчатый график
axes[1, 0].step(x, np.sin(x), where='mid', linewidth=2)
axes[1, 0].set_title('Ступенчатый график')

# 4. График с заливкой
axes[1, 1].fill_between(x, np.sin(x), np.cos(x), alpha=0.5)
axes[1, 1].set_title('График с заливкой')

plt.tight_layout()
plt.show()