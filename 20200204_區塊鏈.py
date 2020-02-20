from hashlib import sha256

x = 5

for i in range(10):
    y = 0

    while sha256(str(x * y).encode()).hexdigest()[:2] != "00":
        y += 1

    x = y
    print('The solution is y = ' + str(y))
