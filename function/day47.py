# import time
# from threading import Thread
#
#
# class Task1(Thread):
#     def run(self):
#         for i in range(3):
#             print("user logged in ")
#             time.sleep(3)
#             print("performing net banking")
#             time.sleep(3)
#             print("Collect ur cash")
# class Task2(Thread):
#     def run(self):
#         for i in range(5):
#             print("DCL")
#             time.sleep(3)
# class Task3(Thread):
#     def run(self):
#         x= 10000
#         y = 20000
#         z = x+y
#         print(z)
#
# t1 = Task1()
# t2 = Task2()
# t3 = Task3()
# t1.start()
# t2.start()
# t3.start()
from threading import Thread


class MSword(Thread):
    def run(self):
        if self.name =="Typing":
            self.typing()
        elif self.name =="Spellcheck":
            self.spellCheck()

        else:
            self.autosave()
    def typing(self):
        for i in range(3):
            print("Typing is in progress")
    def spellCheck(self):
        for i in range(3):
            print("spell check is in progress")

    def autosave(self):
        print("auto save in progress")
m1 = MSword()
m2 = MSword()
m3 = MSword()

m1.name = "Typing"
m2.name = "Spellcheck"
m3.name = "Autosave"
m1.start()
m2.start()
m3.start()
