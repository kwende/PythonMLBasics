import matplotlib.pyplot as plt
import numpy as np

np.random.seed(22)

N = 1000
xRange = np.arange(0, 100, 1)
random_y = [np.random.normal(x, 15) * 3.5 - 25 for x in xRange]

m = 2.5
b = 150
c = 0
for i in range(0, 1100):
    mSum = 0
    bSum = 0
    for x in range(0, len(random_y)):
        mErr = ((x * m + b) - random_y[x]) * x
        mSum = mSum + mErr

        bErr = ((x * m + b) - random_y[x])
        bSum = bSum + bErr

    averageErrorWrtM = 2 * (mSum / len(random_y))
    m = m - (.0001 * averageErrorWrtM)

    averageErrorWrtB = 2 * (bSum / len(random_y))
    b = b - (.01 * averageErrorWrtB)

    # this is drawing code and the modulo and < 20 are there 
    # just to make the animation clearer.     
    if i < 20 or i % 5 == 0:
        plt.scatter(x = xRange, y = random_y)
        plt.plot(xRange, xRange * m + b, 'r')

        print(str(b) + "," + str(m))

        plt.xlabel("X")
        plt.ylabel("Y")

        plt.savefig(str(c) + "_fig.jpeg")

        c = c + 1

        plt.close()
