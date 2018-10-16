import matplotlib.pyplot as plt
import numpy as np

np.random.seed(22)

treeTypeA = np.array([np.random.normal(100, 25) for _ in range(0,5000)])
treeTypeB = np.array([np.random.normal(300, 15) for _ in range(0,5000)])
combined = np.append(treeTypeA, treeTypeB)

max = np.amax(treeTypeA)

def Accuracy(typeA, typeB, m, b):
    numRight = ((typeA * m + b) < 0).sum()
    numRight = numRight + (((typeB * m + b) >= 0).sum())

    return numRight / (len(typeA) + len(typeB))

m = 1
b = 1
k = 0
lastAccuracy = 0

mHistory = []

while True:

    mSum = np.sum(((treeTypeA * m + b) - -1) * treeTypeA) + np.sum(((treeTypeB * m + b) - 1) * treeTypeB)
    bSum = np.sum((treeTypeA * m + b) - -1 ) + np.sum((treeTypeB * m + b) - 1 )

    mErr = 2 * (mSum / (len(treeTypeA) + len(treeTypeB)))
    bErr = 2 * (bSum / (len(treeTypeA) + len(treeTypeB)))

    m = (m - mErr * .00001)
    b = (b - bErr * .00001)

    accuracy = Accuracy(treeTypeA, treeTypeB, m, b)

    if k % 5000 == 0:
        print()
        print(str(m) + "x + " + str(b))
        print("Iteration " + str(k) + ": " + str(accuracy * 100.0))
        lastAccuracy = accuracy

    if accuracy == 1:
        break

    k = k + 1

print("Took " + str(k) + " iterations")
print("y = " + str(m) + "x + " + str(b))

#plt.scatter(x = np.arange(0, len(mHistory)), y = mHistory)

#classes = np.apply_along_axis(lambda x: m * x + b, 0, combined)
#classesHist = np.histogram(classes, bins=2)

#plt.bar(classesHist[1][0:len(classesHist[1]) - 1], classesHist[0])
#plt.show()
#plt.scatter(x = xRange, y = random_y)
