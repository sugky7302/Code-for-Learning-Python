a = 10
a1 = 7
b = {int(a) & v for v in [1, 2, 4, 8]} - {0}
c = {int(a1) & v for v in [1, 2, 4, 8]} - {0}
d = set()
print(b)
print(c)
print(d)
print(b.isdisjoint(c))
print(c.isdisjoint(d))
