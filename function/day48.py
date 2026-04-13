# import time
# from threading import Thread
# class MSword(Thread):
#     def run(self):
#         for i in range(5):
#             if self.name =="Typing":
#                 self.typing()
#             elif self.name =="Spellcheck":
#                 self.spellCheck()
#             else:
#                 self.autosave()
#     def typing(self):
#         for i in range(5):
#             print("Typing is in progress")
#             time.sleep(5)
#         print("Typing stopped")
#     def spellCheck(self):
#         while True:
#             print("spell check is in progress")
#             time.sleep(5)
#
#     def autosave(self):
#         while True:
#             print("auto save in progress")
#             time.sleep(5)
# m1 = MSword()
# m2 = MSword()
# m3 = MSword()
#
# m1.name = "Typing"
# m2.name = "Spellcheck"
# m3.name = "Autosave"
#
# m2.daemon = True
# m3.daemon = True
#
# m1.start()
# time.sleep(1)
# m2.start()
# time.sleep(1)
# m3.start()
# time.sleep(1)
import threading
import time
from threading import Thread


# import time
# from threading import Thread
#
#
# class Movie(Thread):
#     def run(self):
#         if self.name == "producer":
#             self.producing()
#         elif self.name == "director":
#             self.directing()
#         elif  self.name == "actor":
#             self.acting()
#         else:
#             self.supporting()
#
#     def producing(self):
#         for i in range(5):
#             print("vijay is producing the movie")
#             time.sleep(5)
#         print("vijay stopped producing the movie")
#     def directing(self):
#         while True:
#             print("Prashanth neel is directing the movie")
#             time.sleep(5)
#     def acting(self):
#         while True:
#             print("Yash is acting in a movie")
#             time.sleep(5)
#
#     def supporting(self):
#         while True:
#             print("Artist are supporting in a movie")
#             time.sleep(5)
# m1 = Movie()
# m2 = Movie()
# m3 = Movie()
# m4 = Movie()
#
# m1.name = "producer"
# m2.name = "director"
# m3.name = "actor"
# m4.name = "artist"
#
# m2.daemon = True
# m3.daemon = True
# m4.daemon = True
#
# m1.start()
# time.sleep(1)
# m2.start()
# time.sleep(1)
# m3.start()
# time.sleep(1)
# m4.start()
# time.sleep(1)

class MSword:
    def run(self):
        if threading.current_thread().name == "Typing":
            print(threading.current_thread().name)
            self.typing()
        elif threading.current_thread().name == "spellcheck":
            self.spellcheck()
        else:
            self.autosave()
    def typing(self):
        for i in  range(3):
            print("Typing is in progress")
            time.sleep(3)
        print("Typing Stopped")
    def spellcheck(self):
        while True:
            print("spell check is in progress")
            time.sleep(3)
    def autosave(self):
        while True:
            print("Auto save is in progress")
            time.sleep(3)
ms = MSword()
t1 = Thread(target=ms.run,name="Typing")
t2 = Thread(target=ms.run,name="spellcheck")
t3 = Thread(target=ms.run,name="autosave")
print(ms.run)
t2.daemon = True
t3.daemon = True
t1.start()
time.sleep(1)
t2.start()
time.sleep(1)
t3.start()
