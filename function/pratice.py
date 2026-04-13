# class book:
#     def __init__(self):
#         self.__pages = None
#     def setpages(self,p):
#         if p>0:
#             self.__pages = p
#         else:
#             print("invalid pages")
#     def getpages(self):
#         return self.__pages
# b = book()
# b.setpages(10)
# print("the pages is",b.getpages())

class Animals:
    legs = 4
    @classmethod
    def walk(cls,name,legs):
        cls.legs = legs
        print(name,"walks with",cls.legs,"legs")

a = Animals()
Animals.walk("tiger",4)
a.walk("human" ,2)




