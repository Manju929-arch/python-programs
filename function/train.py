class Train:
    seat =100
    def __init__(self):
       a =int(input("Enter the number of seats"))
       Train.seat =Train.seat-a
       print("available seta is ", Train.seat)

t1 = Train()
t2 = Train()
t3 = Train()
print(" Total available Seat available is",Train.seat)

