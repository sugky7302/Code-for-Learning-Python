def a():
    return 1, 2

b = {'a': a}
c, d = b['a']()
print(c)
