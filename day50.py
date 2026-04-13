# import threading
# import time
# from threading import Thread, current_thread
# from threading import Thread,Lock
#
#
# class House:
#     def __init__(self):
#         self.lock  = threading.Lock()
#         t1 = Thread(target=self.run,name="Boy")
#         t2 =Thread(target=self.run, name="Girl")
#         t3 = Thread(target=self.run, name="Other")
#
#         t1.start()
#         time.sleep(1)
#         t2.start()
#         time.sleep(1)
#         t3.start()
#     def run(self):
#         with self.lock:
#             print(current_thread().name,"has Entered the bathroom")
#             time.sleep(4)
#             print(current_thread().name,"has closed the door")
#             time.sleep(4)
#             print(current_thread().name,"has Bath")
#             time.sleep(4)
#             print(current_thread().name,"has dressed up")
#
# h = House()
from threading import Thread


class House:
    def run(self):

    def enter(self):
        print("Enter the  bathroom")
    def closed(self):
        print("Closed the door")
    def Bath(self):
        print("Bathed")

H = House()
t1 = Thread(target=H.run ,name= "boy")
t2 = Thread(target=H.run, name = "girl")
t3 = Thread(target=H.run, name= "Other")


