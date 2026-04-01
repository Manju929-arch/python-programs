class Restaurant:
    def __init__(self,restaurent_name,cuisine_type):
        self.restaurent_name = restaurent_name
        self.cuisine_type = cuisine_type

    def describe_restaurent(self):
        print("the restaurent is open",self.restaurent_name)
r = Restaurant("sagar hotel","masala dosa")
r.describe_restaurent()
print(r.restaurent_name ,r.cuisine_type)