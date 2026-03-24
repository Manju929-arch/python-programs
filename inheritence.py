
class Card:
    def __init__(self, card_no, exp, cvv):
        self.card_no = card_no
        self.exp = exp
        self.cvv = cvv
        self.balance = 0

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print("Withdrawn:", amount)
        else:
            print("Insufficient balance")

    def swipe(self, amount):
        print("Swiped for:", amount)

    def checkBal(self):
        print("Balance:", self.balance)



class CreditCard(Card):
    def __init__(self, card_no, exp, cvv, credit_limit):
        super().__init__(card_no, exp, cvv)
        self.credit_limit = credit_limit

    def payBills(self, amount):
        print("Bill paid:", amount)



class DebitCard(Card):
    def deposit(self, amount):
        self.balance += amount
        print("Deposited:", amount)



class ForexCard(Card):
    def loadAmount(self, amount):
        self.balance += amount
        print("Loaded amount:", amount)

    def convertAmount(self, rate):
        print("Converted balance:", self.balance * rate)


# Creating Objects
d = DebitCard("1234", "12/28", "123")
d.deposit(5000)
d.withdraw(1000)
d.checkBal()

c = CreditCard("5678", "10/27", "456", 10000)
c.swipe(2000)
c.payBills(2000)

f = ForexCard("9999", "09/29", "789")
f.loadAmount(3000)
f.convertAmount(0.012)