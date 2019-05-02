import numpy as np 

a = np.random.rand(8, 7)
shape = a.shape

d = 0
for i in range(3, 5) :
    avg = 0

    b = a[i,:]
    c = b[np.argsort(b)]

    print(b)
    print(c)
    for j in range(1, c.shape[0] - 1) :
        avg += c[j]

    d = avg / (c.shape[0]-2)

print(d)
    