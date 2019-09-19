a = [x for x in range(1, 10)]
b = [2*y for y in range(15)]

print(min(a), max(a))
print(a+b)
print(2*a)

c = {"a": 1, "b": 2}
c.setdefault("c", 3)
print(c.get("c"))

a = 1
while a < 5:
    if a == 10:
        break
    a += 1
else:
    print("hihi")

def f(x, y=[]):
    y.append(x)
    return y, id(y)

print(f(20))
print(f(25))

