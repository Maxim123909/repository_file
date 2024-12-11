#Сложный уровень первая задача
num_1 = int(input('Высота первого параллепипеда: '))
num_2 = int(input('Длина  первого параллепипеда: '))
num_3 = int(input('Ширина первого параллепипеда: '))
num_4 = int(input('Высота второго параллепипеда: '))
num_5 = int(input('Длина  второго параллепипеда: '))
num_6 = int(input('Ширина второго параллепипеда: '))
num_7 = int(input('Высота третьего параллепипеда: '))
num_8 = int(input('Длина  третьего параллепипеда: '))
num_9 = int(input('Ширина третьего параллепипеда: '))
V = num_1 * num_2 * num_3 + num_4 * num_5 * num_6 + num_7 * num_8 * num_9
print(f'Объём трех параллепипедов: ', V)
#Вторая задача
num_10 = int(input('Введите число: '))
num_11 = 0
while num_11 != 10:
            num_11 += 1
            t = num_10 * num_11
            print(str(t))
#Третья задача
from scipy.optimize import minimize
def num_12(x):
    return x**2 - 4*x + 4
result = minimize(num_12, x0=0) #Эту строчку я подсмотрел в интернете
print(result.x)
