import numpy as np

A = np.array([[1, 2, 3, 4, 5, 6], [6, 5, 4, 3, 2, 1], [1, 2, 3, 4, 5, 6],
              [6, 5, 4, 3, 2, 1], [1, 2, 3, 4, 5, 6], [6, 5, 4, 3, 2, 1]])
B = np.array([[1, 0, -1], [1, 0, -1], [1, 0, -1]])

print(A)
print(B)

# 卷積(convolution)運算
c = np.zeros((A.shape[0] - B.shape[0] + 1, A.shape[1] - B.shape[1] + 1))
for m in range(A.shape[0] - B.shape[0] + 1):
    for n in range(A.shape[1] - B.shape[1] + 1):
        for i in range(B.shape[0]):
            for j in range(B.shape[1]):
                c[n][m] = c[n][m] + A[n + i][m + j] * B[i][j]

print(c)

D = np.array([[1, 2], [3, 4]])
E = np.zeros((4, 4))
E[1:3, 1:3] = D
print(E)