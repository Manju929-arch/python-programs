#
# operator overloading
#
# __add__()
# __sub__()
# __mul__()
# __div__()
# __truedev__()
# __lt__()
# __gt__()
# __le__()
# __eq__()
from abc import abstractmethod


# class Employee:
#     def __init__(self,name):
#         self.name = name
# e1 = Employee("john")
# print(e1)
# <__main__.Employee object at 0x0000018F19728590>
# class student:
#     def __init__(self,fees):
#         self.fees =fees
#     def __add__(self, other):
#         return student(self.fees+other.fees)
#     def __str__(self):
#         return str(self.fees)
#
# s1 = student(100000)
# s2 = student(75000)
# s3 = student(200000)
# s4 = student(30000)
# print(s1+s2+s3+s4)



from abc import ABC, abstractmethod

class Demo(ABC):
    @abstractmethod
    def meth(self):
        pass


