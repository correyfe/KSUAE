# sum=0
# k=(10,8,29,35,7)
# print("Kortage: ")
# for i in k:
#     print(i, end=' ')
# for i in range(5):
#     if k[i]>=10:
#         sum+=k[i]
# print('\nSum=', sum)

# pr=1
# k=(10,8,29,35,7)
# print("Kortage: ")
# for i in k:
#     print(i, end=' ')
# for i in range(5):
#     if k[i]>=10:
#         pr*=k[i]
# print('\npr=', pr)

# a=-32768
# b=32767
# k=(10,8,29,35,7)
# for i in k:
#     print(i, end=' ')
# for i in range(5):
#     if k[i]>a:
#         a=k[i]
#     if k[i]<b:
#         b=k[i]

# print('\n',a, b)

# pr=1
# k=(10,8,29,35,7)
# print("Kortage: ")
# for i in k:
#     print(i, end=' ')
# for i in range(5):
#     if k[i]>=10:
#         pr*=k[i]
# print('\npr=', pr)

# a=-32768
# b=32767
# k=(10,8,29,35,7)
# for i in k:
#     print(i, end=' ')
# for i in range(5):
#     if k[i]>a:
#         a=k[i]
#     if k[i]<b:
#         b=k[i]

# print('\n',a, b)
# a,b=b,a
# print(a, b)

# k=(10,15,6,35,4,5,23,5)

# a=int(input('from: '))
# b=int(input('to: '))
# print(k[a:b])

# korteg=(-11, -12, 35, -8, -25, 39, 0, -12)

# for i in korteg:
#     print(i, end=' ')
# kol=0
# proizv=1
# for i in range(8):
#     if i%2==1 and korteg[i]<0:
#         proizv*=korteg[i]
#         kol+=1
# print(proizv, kol)

# import math

# korteg=(-11, -12, 35, -8, -25, 39, 0, -12)
# kol=0
# sum=0
# for i in range(8):
#     if korteg[i]>=0:
#         sum+=pow(korteg[i], 2)
#         kol +=1
#         sr=sum/kol
# print(sr, kol)

# import matplotlib.pyplot as plt

# x=[1,2,3,4,5]
# y=[1,4,9,16,25]
# plt.plot(x,y)
# plt.title("Graph")
# plt.xlabel('X axe')
# plt.ylabel("y axe")
# plt.grid(True)
# plt.show()

# import matplotlib.pyplot as plt
# import numpy as np

# x= np.linspace(0,10,100)
# y=np.sin(x)

# plt.figure(figsize=(8,4))
# plt.plot(x,y,label='sin(x)')
# plt.xlabel('x')
# plt.ylabel('sin(x)')
# plt.grid(True, alpha=0.3)
# plt.show()
