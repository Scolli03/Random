import numpy
import matplotlib.pyplot as plt

x = numpy.random.normal(5.0, 1.0, 9)
y = numpy.random.normal(10.0, 2.0, 9)

plt.scatter(x, y)
plt.show()

input()