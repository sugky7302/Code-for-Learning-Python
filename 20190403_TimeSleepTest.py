import time

HZ = 0.01
TIME = 1
start = time.perf_counter()
c = 0
while time.perf_counter() - start < TIME:
    c += 1
    pass

print("cost {} s, cpu is runned {} times".format(time.perf_counter() - start, c))
