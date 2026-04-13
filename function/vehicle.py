class vehicle:
    wheels = 4
    @classmethod
    def run(cls,name,wheels):
        cls.wheels = wheels
        print(name,"Has the wheels of",cls.wheels)

a =vehicle()
a.run("Bike",wheels=2)
a.run("Truck",4)