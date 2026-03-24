class Car:
    def start(self):
        print("Car starting")

    def shift(self, gn):
        print("Gear shifted to", gn, "gear")
        if gn == 0:
            self.stop()

    def stop(self):
        print("Car stopped")


class Driver:
    def drive(self):
        self.c = Car()
        self.c.start()
        self.c.shift(1)
        self.c.shift(2)
        self.c.shift(3)

        print("Driver drives with high speed")


        self.c.shift(0)


# Creating object
d = Driver()
d.drive()
