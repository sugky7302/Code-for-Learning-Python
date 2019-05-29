class test:
    def __init__(self):
        self.a, self.b, self.c, self.d = self.__test()

    def __test(self):
        return 1, 2, 3, 4


def main():
    aa = test()
    print(aa.a, aa.b, aa.c, aa.d)


if __name__ == "__main__":
    main()