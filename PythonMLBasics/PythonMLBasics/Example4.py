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

def sigma(em, bee, x):
    return 1 / (1 + np.exp(-1 * (em * x + bee)))

def rhs_theta(em, bee, x, y):
    return np.sum((sigma(em, bee, x) - y) * (sigma(em, bee, x) * (1 - sigma(em, bee, x)) * x))

def rhs_b(em, bee, x, y):
    return np.sum((sigma(em, bee, x) - y) * (sigma(em, bee, x) * (1 - sigma(em, bee, x))))

while True:

    mSum = rhs_theta(m, b, treeTypeA, -1) + rhs_theta(m, b, treeTypeB, 1)
    bSum = rhs_b(m, b, treeTypeA, -1) + rhs_b(m, b, treeTypeB, 1)

    mErr = 2 * (mSum / (len(treeTypeA) + len(treeTypeB)))
    bErr = 2 * (bSum / (len(treeTypeA) + len(treeTypeB)))

    m = (m - mErr * .001)
    b = (b - bErr * .001)

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