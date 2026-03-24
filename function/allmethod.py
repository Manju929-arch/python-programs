class BankAccount:
    bank_name = "State Bank"
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance

    def show_balance(self):
        print("Account Holder:", self.name)
        print("Balance:", self.balance)

    @classmethod
    def bank_details(cls,number,address):
        cls.number = number
        cls.address=address
        print("Bank Name:", cls.bank_name, "\n phone number :", cls.number ,"\n Address:",cls.address)


    @staticmethod
    def bank_rules():

        print("Minimum balance should be 1000")

a1 = BankAccount("Manju", 5000)
a1.show_balance()
BankAccount.bank_details(1234567890,"Bengalore")
BankAccount.bank_rules()