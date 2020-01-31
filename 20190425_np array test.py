import math
import numpy as np

print(math.radians(370))
a = np.random.rand(7, 8)
b = np.random.rand(7)
print(b.shape[0])
print(np.concatenate((b, np.array([2])), axis=0))
c = np.array([1, 2, 3, 4, 5, 6, 7])
print(np.concatenate((a, c.reshape(c.shape[0], 1)), axis=1))
shape = a.shape

d = 0
for i in range(3, 5):
    avg = 0

    b = a[i, :]
    c = b[np.argsort(b)]

    # print(b)
    # print(c)
    for j in range(1, c.shape[0] - 1):
        avg += c[j]

    d = avg / (c.shape[0] - 2)

# print(d)

a = np.ones((4, 2))
print("")
print(a[3])
b = np.array([[2, 3]])
# print(np.concatenate((a, b), axis=0))
# print(np.array(b.shape))
print([5]*3)
