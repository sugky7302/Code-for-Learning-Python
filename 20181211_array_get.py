import numpy as np

x = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])
y = np.array([[1, 0], [0, 1]])
# 希望效果: 0, 0, y[0, 0]
#         0, 1, y[0, 1]
#         1, 0, y[1, 0]
y = y.reshape(y.shape[0] * y.shape[1], 1)
print(y.shape)
# print(x[ :, :, y[]])

k = 0
z = np.zeros((y.shape[0]ㄩ, 1))
print(z.shape)
print(x.shape[0])
print(x.shape[1])
for i in range(x.shape[0]):
    for j in range(x.shape[1]):
        z[k, 0] = x[i, j, y[k, 0]]
        k = k + 1

print(z)