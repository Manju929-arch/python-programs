class pen:
    def __init__(self,price):
        self.price = price

    def __add__(self, other):
        return self.price + self.other
    def __sub__(self, other):
        return self.price - self.other
    