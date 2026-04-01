class Demo :
    def fun1(self):
        print("Inside fun1")
        # try:
        self.fun2()
        # except Exception:
        #     print("Problem in fun1")
    def fun2(self):
        print("Inside fun2")
        a = 0
        b = 0
        c = a/b
        print("Div is ",c)
print("Entering main logic")
d = Demo()
try:
    d.fun1()
except Exception:
    print("Problem in main logic")
print("Exiting pgm normally")
# output 1
# Entering main logic
# Inside fun1
# Inside fun2
# Problem in fun1
# Exiting pgm normally

# output 2
# Entering main logic
# Inside fun1
# Inside fun2
# Problem in main logic
# Exiting pgm normally