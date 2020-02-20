a = {"a": [1, 2], "b": 2, "c": 3}
for k in a:
    print(k)

b = [9, 8, 7, 6, 5, 4]
for k, v in enumerate(b):
    print(k, v)

for v in b:
    print(v)


class List(list):
    pass


c = ["1", "2", "3", "4"]
print(List(e for e in c))
from collections import OrderedDict as ODict

a = ODict({"a": 1})
print(a)
print(isinstance(a, ODict))
