class C1:
    def __init__(self):
        print(1)

class C2:
    def __init__(self):
        print(2)

class C3:
    def __init__(self):
        print(3)


def hi(k):
    test = {
        0 : C1,
        1 : C2,
        2 : C3
    }

    c = test.get(k, None)

    if c:
        return c()

    return None

def a():
    return 1, 2, 3, 4, 5

def main():
    k = hi(2)
    t = a()
    print(type(t), t)

if __name__ == "__main__":
    main()
