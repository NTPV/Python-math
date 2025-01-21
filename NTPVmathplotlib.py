import matplotlib.pyplot as plt
import numpy

x = numpy.linspace(-10, 10, 100)
y = x**2

plt.plot(x, y, label = 'y = x^2')

plt.title('NTPV Вывод простейшего графика функции при помощи библиотек matplotlib.pyplot и numpy')
plt.xlabel('x')
plt.ylabel('y')

plt.legend()
plt.grid()
plt.show()
