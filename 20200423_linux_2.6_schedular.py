from bitarray import bitarray
from bitarray import util


class MaxProrityQueue:
    def __init__(self, queue=[]):
        self.__queue = queue

    def __iter__(self):
        self.__index = 0
        return self

    def __next__(self):
        if self.__index >= len(self.__queue):
            raise StopIteration

        self.__index += 1
        return self.__queue[self.__index - 1]

    def push(self, item):
        self.__queue.append(item)
        self.__swim(len(self.__queue))
        return self

    def __swim(self, i):
        while i > 1 and self.__less(i // 2 - 1, i - 1):
            self.__exchange(i // 2 - 1, i - 1)
            i = i // 2

    def pop(self):
        max_value = self.__queue[0]
        self.__exchange(0, len(self.__queue) - 1)
        self.__queue.pop()
        self.__sink(0)
        return max_value

    def __sink(self, i):
        while (j := i * 2 + 1) <= (length := len(self.__queue) - 1):
            if j < length and self.__less(j, j + 1):
                j += 1

            self.__exchange(i, j)
            i = j

    def __less(self, i, j):
        return self.__queue[i] < self.__queue[j]

    def __exchange(self, i, j):
        self.__queue[i], self.__queue[j] = self.__queue[j], self.__queue[i]


b = MaxProrityQueue().push((2, "a")).push((3, "b")).push((4, "c"))
for v in b:
    print(v)

print(b.pop())

print(a:=bitarray(15))
print(a.count(1))
print(util.count_n(a, 1))  # 取得第一個True的index
