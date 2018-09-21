import matplotlib.pyplot as plt
import numpy as np

np.random.seed(10)

N = 1000
xRange = np.arange(0, 100, 1)
random_y = [np.random.normal(x, 15) * 9 for x in xRange]

print(random_y[9])

for i in range(0, len(random_y)):
    if random_y[i] < 0:
        random_y[i] = abs(random_y[i])

plt.scatter(x = xRange, y = random_y)
plt.plot(xRange, xRange * 2, 'r')

plt.xlabel("Days")
plt.ylabel("# of Apples")
plt.show()