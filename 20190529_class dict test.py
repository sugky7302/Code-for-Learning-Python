import traceback
import threading

class C1:
    def __init__(self):
        print(1)

class C2:
    aaaa = 1

    def __init__(self):
        print(id(self.aaaa))
        self.aaaa = 2
        print(id(self.aaaa))


class C3:
    __a = 5

    def __new__(cls, *args, **kwargs):
        print(cls.___a)

    def __init__(self):
        print(self.__class__.__a)


def hi(k):
    test = {
        0 : C1,
        1 : C2,
        2 : C3
    }

    c = test.get(k, None)

    if c:
        try:
            return c()
        except Exception as e:
            print(type(e))

    return None

def a():
    return 1, 2, 3, 4, 5

def main():
    k = hi(2)
    # print(0 < 1 < 2)

if __name__ == "__main__":
    main()
    a = "0,232,4,623,34,45"
    print(a[0])
    a = a.split(',')
    print(a[2])

class A:
    def b(self):
        self.B.c()

class B:
    def __init__(self, A):
        self.A = A
        A.B = self
    
    def c(self):
        print("hi")

# B(p := A())
# p.b()

class P:
    def __init__(self):
        self.a = 10

    def b(self):
        print(self.a)

class Q(P):
    A = 1
    B = 2

    def __init__(self):
        super().__init__()  # self = P.__init__(self)
        self.t = 5

    def b(self):
        print(self.B)
        super().b()  # P.b(self)
        print(self.a + self.t)

q = Q()
q.b()
print(['1'] == ['4'])


# NOTE: 2020-03-27
#   必須要繼承object才能使用單例模式
#   必須要在同一個python執行器下
#   目前測試沒加鎖也沒有網路上所說的，不支援多線程的問題，再多注意
#   單例模式的另一個做法是在類別下面生成一個實例，其他文件就import那個實例
class R(object):
    # _instance_lock = threading.Lock()

    def __new__(cls, *args, **kwargs):
        if not hasattr(R, "_instance"):
            # with R._instance_lock:
                # if not hasattr(R, "_instance"):
            R._instance = object.__new__(cls, *args, **kwargs)
        return R._instance

    def __init__(self):
        import time
        time.sleep(2)


def task(arg):
    obj = R()
    print(obj)


for i in range(20):
    t = threading.Thread(target=task, args=[i, ])
    t.start()
