class Test:
    count =0
    def __init__(self):
        Test.count = Test.count+1
t1 = Test()
t2 = Test()
t3 = Test()
t4 = Test()
t5 = Test()
print("Total Number of objects is ",t1.count)
print("Total number of objects is ",Test.count)