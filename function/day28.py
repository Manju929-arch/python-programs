class Employee:
    def __init__(self):
        self.__sal = None
    @property   #make method to use a s avaiable usages
    def sal(self):
        return self.__sal
    @sal.setter # makes method to access like a variable to assign value
    def sal(self,s):
        if s>0:
            self.__sal =s
        else:
            print("Invalid salaries")
e = Employee()
e.sal = 10000  # e.sal : accessing setter function like a varaible
print("the sa is ", e.sal) # retrieving the value like a variable
