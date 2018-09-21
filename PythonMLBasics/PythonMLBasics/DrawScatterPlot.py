import matplotlib.pyplot as plt
import numpy as np

np.random.seed(10)

N = 1000
xRange = np.arange(0, 100, 1)
random_y = [np.random.normal(x, 15) * 9 for x in xRange]

for i in range(0, len(random_y)):
    if random_y[i] < 0:
        random_y[i] = abs(random_y[i])

slope = 2
for i in range(0, 190):
    print(i)
    sum = 0
    for x in range(0, len(random_y)):
        err = ((x * slope) - random_y[x]) * x
        sum = sum + err
    error = sum / len(random_y)
    slope = slope - (.00001 * error)

    plt.scatter(x = xRange, y = random_y)
    plt.plot(xRange, xRange * slope, 'r')

    plt.xlabel("Days")
    plt.ylabel("# of Apples")
    
    plt.savefig(str(i) + "_fig.jpeg")
    plt.close()
