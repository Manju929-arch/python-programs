# #
# # print("Entering the prg")
# # age= int(input("Enter the age "))
# # try:
# #     if age >=18:
# #         print("you are eligible for drivring licence")
# #     else:
# #         raise Exception()
# # except Exception:
# #     print("you are not eligible for driving licences")
# # print("Exiting pgm normally")
# class invalid_age_Exception:
#     pass
# class licence:
#     def __init__(self):
import time


# class UnderAgeException(Exception):
#     pass
# class OverAgeExceoption(Exception):
#     pass
# class DL:
#     def dispatchDL(self):
#         self.age = int(input("Enter the age"))
#
#         try:
#             if self.age<18:
#                 raise UnderAgeException("DL can't be issued Age is less than 18")
#             elif self.age>60:
#                 raise OverAgeExceoption("DL can't be issude Age is greater than 60")
#             else:
#                 print("collect your DL and age is :",self.age)
#         except UnderAgeException as e:
#             print(e)
#
#         except OverAgeExceoption as e:
#             print(e)
# d = DL()
# d.dispatchDL()


class Demo:
    def banking(self):
        self.un = input("Enter the username")
        self.pwd = input("Enter the password")
        print("Collect your cash")
    def printing(self):
        for i in range(5):
            print("Dhee coding lab")
            time.sleep(5)
    def add(self):
        a=10
        b=20
        c = a+b
        print(c)
d = Demo()
d.banking()
d.printing()
d.add()



