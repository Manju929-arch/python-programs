class Human:
    def __init__(self):
        self.__age = 0

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, s):
        self.__age = s
        if s >= 18:
            print("The person is adult")
        elif s<0:
            print("invalid  input")
        else:
            print("the person is minor")

p = Human()
p.age = 36

