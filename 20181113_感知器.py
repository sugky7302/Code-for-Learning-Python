import numpy as np


def AND(x1, x2):
    input = np.array([x1, x2])
    weight = np.array([0.5, 0.5])
    bias = -0.7
    output = np.sum(weight * input) + bias
    if output > 0:
        return 1
    else:
        return 0


def NAND(x1, x2):
    input = np.array([x1, x2])
    weight = np.array([-0.5, -0.5])
    bias = 0.7
    output = np.sum(weight * input) + bias
    if output > theta:
        return 0
    else:
        return 1


def OR(x1, x2):
    input = np.array([x1, x2])
    weight = np.array([0.5, -0.5])
    bias = 0.2
    output = np.sum(weight * input) + bias
    if output > theta:
        return 1
    else:
        return 0


def XOR(x1, x2):
    s1 = NAND(x1, x2)
    s2 = OR(x1, x2)
    y = AND(s1, s2)
    return y

a = np.random.randn(3, 3)
b = np.random.randn(3, 1)
c = a*b
print(c)
c = np.dot(a, b)
print(c)