a = ((((((1, 2, 3))))))
print(a[0])

def test(count=1):
    if count == 1:
        return 1
    
    return 2

print(test(count=2))

import numpy as np
k = np.ones((2, 3))
r, c = k.shape
print(r, c)