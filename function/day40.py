from abc import ABC,abstractmethod
class shape(ABC):
    def __init__(self):
        self.area = None
    @abstractmethod
    def input(self): # Abstract Method
        pass
    @abstractmethod
    def calArea(self): # Abstract Method
        pass
    def disp(self):
        print("Area is",self.area) #Concreate Method

class Square(shape):
    def input(self):
        self.l = int(input("Enter the length of the square"))
    def calArea(self):
        self.area = self.l*self.l
class Rectangle(shape):
    def input(self):
        self.l = int(input("Enter the length of the rectangle"))
        self.b  = int(input("Enter the width of hte tectangle:"))

    def calArea(self):
        self.area = self.l *self.b
class Circle(shape):
    def input(self):
        self.r = int(input("Enter the radius of the circle:"))

    def calArea(self):
        self.area = 3.14*self.r*self.r


