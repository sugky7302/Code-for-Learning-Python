def unpack(x, y, z):
    print(x, y, z)


a = [1, 2, 3]
unpack(*a)

b = {'x': 1, 'y': 2, 'z': 3}

unpack(*b)  # NOTE: 傳key
unpack(**b)  # NOTE: 傳值


def multi():
    return 1, 2


def test(a, b):
    k = [a, b]
    print(id(k))
    return k


c = test(*multi())
print(id(c))
