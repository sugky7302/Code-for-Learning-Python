import math
import numpy as np
import time

# for i in range(1, 5):
#     angle = math.pi / 2 * i
#     print(math.cos(angle))
#     print(math.sin(angle))
# print(" ")
angle = 1.32
x = (-0.132275998592 + 0.411435008049) / math.cos(angle)
y = (2.19178891182 - 1.10009694099) / math.sin(angle)
print(x, y)


def sin_cos(rad):
    _, quotient = math.modf((abs(rad - 0.0001) + math.pi) / (2 * math.pi))
    ans = rad - math.copysign(1, rad) * quotient * (2 * math.pi)
    # print(quotient, ans)
    return ans


a = math.pi * -1.3
b = math.pi * 0.8
for i in range(0, 81):
    if abs(sin_cos(a) - sin_cos(b)) < (math.pi / 180):
        print(i)

    a += math.pi * 0.05

print(math.radians(18) * 90 / 340)

print(math.radians(90))
print(math.radians(4.5))
# start = time.time()

# for i in range(1000000):
#     x = np.random.random(2)
#     y = np.random.random(2)
#     d = np.sqrt(np.sum(np.square(x-y)))
# print("{:.8f}".format(time.time()-start))

# start = time.time()

# for i in range(1000000):
#     x = np.random.random(2)
#     y = np.random.random(2)
#     d = np.linalg.norm(x-y)
# print("{:.8f}".format(time.time()-start))
