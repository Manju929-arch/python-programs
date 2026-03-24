class OS:
    def __init__(self):
        print("OS is created")
    def checkOS(self):
        print("OS is  Working")
class Charger:
    def __init__(self):
        print("Charger is creadted")
    def getCharger(self):
        print("Charger can be used for charging")
class Mobile:
    def __init__(self):
        self.o = OS()
        print("Mobile is created with os installed")
    def hasA(self,ch):
        print("Charger acquired")


m = Mobile()
c = Charger()
m.hasA(c)
m.o.checkOS()
c.getCharger()
m = None
c.getCharger()