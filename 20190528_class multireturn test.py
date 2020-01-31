class test:
    def __init__(self):
        self.a, self.b, self.c, self.d = self.__test()

    def __test(self):
        return 1, 2, 3, 4

    def kk(self):
        print("ha")


class test1(test):
    def __init__(self):
        super().__init__()


def main():
    aa = test1()
    print(aa.a, aa.b, aa.c, aa.d)
    aa.kk()


if __name__ == "__main__":
    main()
