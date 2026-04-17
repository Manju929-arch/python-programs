
from threading import Thread,Lock,current_thread #imorting  the  Lock and current thread
import time
class DBprocess:
    def __init__(self):
        self.r1 = Lock()
        self.r2 = Lock()
        self.r3 = Lock()
    def run(self):
        if current_thread().name == "Rama":
            self.aquire_rama_resource()
        else:
            self.aquire_sita_resource()

    def aquire_rama_resource(self):
        with self.r1:
            print("Rama quired Orcale ")
            time.sleep(1)
            with self.r2:
                print("Rama aquired sybasse")
                time.sleep(1)
                with self.r3:
                    print("Rama aquired informics")

    def aquire_sita_resource(self):
        with self.r3:
            print("sita aquire informics")
            time.sleep(1)
            with self.r1:
                print("sita aquire sybase")
                time.sleep(1)
                with self.r2:
                    print("sita aquired oracle")
db = DBprocess()
t1 = Thread(target=db.run, name="Rama")
t2 = Thread(target=db.run, name="sita")  #explicit threading is add
t1.start()
time.sleep(1)
t2.start()


