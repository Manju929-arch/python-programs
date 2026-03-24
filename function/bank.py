class Bankaccount:
    def attribute(self,account_holder,balance):
        self.account_holder = account_holder
        self.balance = balance
        print("current balance is",self.balance)
    def deposit(self,amount):
        self.balance+=amount
        print(amount,"deposited successfully")
        print("Total balance is ",self.balance)

    def withdraw(self,amount):
        if amount<=self.balance:
            self.balance -= amount
            print(amount,"withdrawn successfully")
        else:
             print("Not enough money")
    def display_balance(self):
        print(f"Account Holder: {self.account_holder}")
        print(f"Current Balance: {self.balance}")
a=Bankaccount()
a.attribute("MANJUNATH G",20000)
a.deposit(10000)
a.withdraw(2000)
a.display_balance()



