class Bank:
    def deposit(self,amount):
        self.balance =self.balance +amount
        if amount>0:
           print(self.balance,"deposit successfully",amount)
        else:
            print("Deposit amount should be always positibe")
    def withdraw(self,amount):
        if amount<=0:
            print("withdraw amount should be always positive")
        elif amount>self.balance:
            print("bal should be greater than amount ")
        else:
            self.balance =self.balance -amount
            print("withdraw amount has been made")
            print("with drawn amount is ",amount)
            print("updated balance is ",self.balance)
    def diplay(self):
        print("current balance is",self.balance)

b1=Bank()
b1.accountholder ="Manjunath G"
b1.balance =100
print("Account Holder is ",b1.accountholder)
print("initial balance is ",b1.balance)
b1.deposit(5000)
b1.withdraw(1000)
b1.diplay()
