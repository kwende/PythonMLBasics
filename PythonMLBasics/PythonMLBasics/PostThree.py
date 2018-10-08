import matplotlib.pyplot as plt
import numpy as np
import math

np.random.seed(10)

randomX = np.random.rand(25) * 10
randomY = np.random.rand(25) * 10

withClasses = []
for i in range(0, len(randomX)):
    y = 1.2 * randomX[i] + 2

    if randomY[i] > y:
        withClasses.append([randomX[i], randomY[i], 1])
    else:
        withClasses.append([randomX[i], randomY[i], -1])

weight = 0
bias = 0
learningRate = .001
#for i in range(0, 100):
#    wErr = 0
#    bErr = 0
#    for d in range(0, len(blue)):
#        v = weight * blue[d][0] + bias
#        if v < 0:
#            wErr = learningRate * (1) * 

#    for d in range(0, len(red)):
#        v = weight * red[d][0] + bias
#        if v >= 0:
#            wErr = learningRate * (-1)

#    mse = (errSum * errSum) / (len(blue) + len(red))
#    weight = weight - ()


plt.scatter(x = [a[0] for a in withClasses if a[2] == 1], y = [a[1] for a in withClasses if a[2] == 1], color = 'b')
plt.scatter(x = [a[0] for a in withClasses if a[2] == -1], y = [a[1] for a in withClasses if a[2] == -1], color = 'r')
plt.plot()

plt.xlabel("x")
plt.ylabel("y")

plt.show()