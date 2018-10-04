import matplotlib.pyplot as plt
import numpy as np

np.random.seed(22)

treeTypeA = np.array([np.random.normal(100, 25) for _ in range(0,5000)])
treeTypeB = np.array([np.random.normal(300, 15) for _ in range(0,5000)])

def Accuracy(typeA, typeB, m, b):
    numRight = ((typeA * m + b) < 0).sum()
    numRight = numRight + (((typeB * m + b) >= 0).sum())

    return numRight / (len(typeA) + len(typeB))

m = 1
b = 1
k = 0
lastAccuracy = 0
while True:

    bSum = 0
    treeTypeAMapped = treeTypeA * m + b
    treeTypeAMapped = np.piecewise(treeTypeAMapped, [treeTypeAMapped < 0, treeTypeAMapped >= 0], [-1, 1])

    treeTypeBMapped = treeTypeB * m + b
    treeTypeBMapped = np.piecewise(treeTypeBMapped, [treeTypeBMapped < 0, treeTypeBMapped >= 0], [-1, 1])

    #treeTypeAMapped = np.array(list(map(convertTo0And1, treeTypeA * m + b)))
    #treeTypeBMapped = np.array(list(map(convertTo0And1, treeTypeB * m + b)))

    #mSum = np.sum(((treeTypeA * m + b) - -1) * treeTypeA) + np.sum(((treeTypeB * m + b) - 1) * treeTypeB)
    #bSum = np.sum((treeTypeA * m + b) - -1 ) + np.sum((treeTypeB * m + b) - 1 )
    mSum = np.sum((treeTypeAMapped - -1) * treeTypeAMapped) + np.sum((treeTypeBMapped - 1) * treeTypeBMapped)
    bSum = np.sum(treeTypeAMapped - -1) + np.sum(treeTypeBMapped - 1)

    mErr = 2 * (mSum / (len(treeTypeA) + len(treeTypeB)))
    bErr = 2 * (bSum / (len(treeTypeA) + len(treeTypeB)))

    m = (m - mErr * .001)
    b = (b - bErr * .001)

    accuracy = Accuracy(treeTypeA, treeTypeB, m, b)

    if k % 1000 == 0:
        print("Iteration " + str(k) + ": " + str(accuracy * 100.0))
        lastAccuracy = accuracy

    if accuracy == 1:
        break

    k = k + 1

print("Took " + str(k) + " iterations")
print("y = " + str(m) + "x + " + str(b))

treeTypeAHist = np.histogram(treeTypeA, bins=100)
treeTypeBHist = np.histogram(treeTypeB, bins=100)


plt.bar(treeTypeAHist[1][0:len(treeTypeAHist[1]) - 1], treeTypeAHist[0])
plt.bar(treeTypeBHist[1][0:len(treeTypeBHist[1]) - 1], treeTypeBHist[0])
plt.show()
#plt.scatter(x = xRange, y = random_y)
