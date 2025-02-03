import matplotlib.pyplot as plt
import numpy as np

#Создаем массив из 50 чисел, равномерно распределенных от 0 до 10
x = np.linspace(0, 10, 100)
y = x

#Строим графики 1 и 2
plt.plot(x, y, 'r--', x, y**2)

#Строим графики 3 и 4 (Первые два массива это x1,y1, вторые два массива это x2,y2)
plt.plot([5,4,3], [7, 8, 9], [2,3,4], [0.5,0.5,0.5])

#Строим график 5
plt.plot([1,2,3,4,5], [4,3,4,5,6], 'r')

#Кастомизируем графики

#Подпись сверху графика
plt.title('Линейная зависимость y = x')
#Подпись оси x и y
plt.xlabel('Ось абсцисс x')
plt.ylabel( 'Ось ординат y')
#Добавляем сетку
plt.grid()

#Выводим все графики
plt.show()
