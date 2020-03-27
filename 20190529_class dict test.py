import traceback

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
