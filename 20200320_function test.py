def a():
    return 1, 2

b = {'a': a}
c, d = b['a']()
print(c)  # 回傳1
k = b['a']()
print(k)  # 回傳(1, 2)
