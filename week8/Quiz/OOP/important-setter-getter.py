class A:
    def __init__(self, x) -> None:
        self.attar = x

    @property
    def attar(self):
        print('getter call')
        return self.__attr

    @attar.setter
    def attar(self, value):
        print('setter call')
        self.__attr = value

    def show(self):
        print(self.__attr)


obj = A(x='x')
obj.show()