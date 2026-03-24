# class Card:
#     def __init__(self,cardNum,exp,cvv):
#         self.cardNum= cardNum
#         self.exp =exp
#         self.cvv =cvv
#
#     def withdraw(self):
#         print("withdrawing an amount")
#     def swipe(self):
#         print("swipping the card")
#     def checkbal(self):
#         print("checking the balance")
# class DebitCard(Card):
#     def deposit(self,amt):
#         print(amt,"deposit using debit card")
# class Creditcard(Card):
#     creditlimit= 100000
#     def paybills(self):
#         print("Bills payed through crdit card")
# class Forexcard(Card):
#     rootCurrency = "INR"
#     targetCurrency =  "USD"
#     def loadAmount(self,amt):
#         print(amt, "loaded using forex card")
#     def converAmount(self):
#         print("converted from ",Forexcard.rootCurrency,"to",Forexcard.targetCurrency)
#
# d = DebitCard("123456789","02/26",123)
# d.deposit(10000)
# d.withdraw()
# d.checkbal()
# d.swipe()
# print("===============================")
# c = Creditcard("123456789","02/26",123)
# c.paybills()
# c.withdraw()
# c.checkbal()
# c.swipe()
# print("credit limit is ",Creditcard.creditlimit)
# print("====================================")
# f = Forexcard("123456789","02/26",123)
# f.checkbal()
# f.loadAmount(1000000)
# f.withdraw()
# f.swipe()
# f.converAmount()

###### write a progarm to vehicla class with the sub class bike car electric vehicle
class vehicle:
    def __init__(self,vehicle_no,brand,fuel_type):
        self.vehicle_n0 = vehicle_no
        self.brand = brand
        self.fuel_type = fuel_type
    def start(self):
        print("Vehicle started")
    def stop(self):
        print("vehicle stopped")
    def displaydetailer(self):
        print("vehicle number",self.vehicle_n0,"Vehicle brand",self.brand,"vehicle fuel type",self.fuel_type)
class Bike(vehicle):
    def kickstart(self):
        print("Bike has kick start")
class Car(vehicle):
    def openTrunk(self):
        print("car has Open Trunk")
class Electric_vehicle(vehicle):
    def chargeBattery(self):
        print(self.vehicle_n0,"is charing")
    def CheckBatteryLevel(self):
        print("Checking battery level")
d = Car("123r","Maruthi","petroleum")
d.displaydetailer()
d.vehicle_n0
d.openTrunk()
d.fuel_type
d.stop()
d.start()
print("=======================================")
d1 = Bike("123r","Honda","petrol")
d1.displaydetailer()
d1.vehicle_n0
d1.fuel_type
d1.stop()
d1.start()
d1.kickstart()
print("=======================================")
d2 = Electric_vehicle("123r","Tesla","Electric battery")
d2.vehicle_n0
d2.start()
d2.stop()
d2.displaydetailer()
d2.chargeBattery()
d2.CheckBatteryLevel()

