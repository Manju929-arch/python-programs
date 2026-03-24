class student:
    def __init__(self):
        self.__marks = None
    def setmarks(self,m):
        if m>=35.0 and m<=100.0:
            self.__marks=m
        else:
            print("Invalid marks/failed")
    def getmarks(self):
        return self.__marks

s1= student()
s1.setmarks(30.5)
print("the marks is ",s1.getmarks())
s2= student()
s2.setmarks(45.5)
print("the marks is ",s2.getmarks())
