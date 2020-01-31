import math 

a = 2
a1 = 10
b = {int(a) & v for v in [1, 2, 4, 8]} - {0}
c = {int(a1) & v for v in [1, 2, 4, 8]} - {0}
d = set()
print(b)
print(str(c))
print(d)
print(b.isdisjoint(c))
print(c.isdisjoint(d))
print(b.issubset(c))

q = 1; p = 2
print(q > p and q or p)
print(math.radians(50))
# for i in range(100):
#     print({int(6.21) & v for v in [0x01, 0x02, 0x04, 0x08]} - {0})
r = "asdfl\r\r\n"
print(r[:-3])

def test(a="1", b=2, c=3, d="k"):
    print(a)
    print(b)
    print(c)
    print(d)

test(5, 1, 6, "haha")
