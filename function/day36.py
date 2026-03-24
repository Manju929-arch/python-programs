class Airtel:
    def recharge(self, CardNum=None, exp=None, cvv=None, username=None, password=None, upiId=None, pin=None):
        if CardNum and exp and cvv:
            print("Recharged by using card")
            print("card num is", CardNum)
        elif username and password:
            print("Recharged by using netBanking")
            print("Username is", username)
        elif upiId and pin:
            print("Recharged by using upi")
            print("upi id is", upiId)
        else:
            print("Invalid input")


a = Airtel()
a.recharge(CardNum=2345678, exp="01/29", cvv=107)
a.recharge(username="Sundra", password="sundra@213")
a.recharge(upiId="21234567890@xyz", pin=1234)
a.recharge()