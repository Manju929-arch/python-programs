class vehicle:
    wheels = 4
    @classmethod
    def run(cls,name,wheels):
        cls.wheels = wheels
        print(name,"Has the wheels of",cls.wheels)
vehicle.run("car",4)
a =vehicle()
a.run("Bike",wheels=2)
a.run("Truck",4)