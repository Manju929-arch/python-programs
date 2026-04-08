print("Entering the pgm")
a = int(input("Enter a : "))
b = int(input("Enter b:"))
try:
     if a>b:
         c = a-b
         print("diff is ",c)
     else:
         raise Exception()
except Exception:
    print("sub not possible ... a<b")
print("Exiting pgm normally")