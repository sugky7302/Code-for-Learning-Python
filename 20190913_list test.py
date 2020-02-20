a = [x for x in range(1, 10)]
b = [2 * y for y in range(15)]

print(min(a), max(a))
print(a + b)
print(2 * a)

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

set1 = {1, 2, 5}
set2 = {5, 7, 9}
print(set1)
set1 ^= set2
print(set1)


def get_primes(N):
    primes = set()
    for n in range(2, N):
        if all(n % p > 0 for p in primes):
            primes.add(n)
            yield n


print(*get_primes(100))

print([i == 2 and 1 or 0 for i in range(8)])

k = 5
a = ["21", "23", "35", "45", "50"]
print(min([float(a[i]) for i in range(4) if 2**i & k > 0]))
print(a[:-1])
b = [1234.5345, 1239.345, 2394.1234, 3482.2189]
print("{}".format([v / 10 for v in b]))

s = "0,0,0,0\r\n"
print(s.strip().split(','))

c = " ".join(["1", "0"])
for k, v in enumerate(c.split(" ")):
    if k > 0:
        print(type(int(v)))
    else:
        print(type(v))
print([k > 0 and int(v) or v for k, v in enumerate(c.split(" "))])
print([int(v) if k > 0 else v for k, v in enumerate(c.split(" "))])
print(1 > 0 and type(int("0") or "0"))

array = ['I', 'love', 'Python']
print([f'{index}: {element}' for index, element in enumerate(array)])
print([(lambda i, v: f'{i}: {v}')(index, element) for index, element in enumerate(array)])

for i in (i for i in range(10) if i > 0):
    print(i)
