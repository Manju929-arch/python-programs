row = 5
for i in range(1, row+1):
    for j in range(1, i+1):
        print("*", end=" ")
    print()

for i in range(1,row+1):
    for j in range(1,i+1):
        print(chr(j+64),end=" ")
    print()
for i in range(1,row+1):
    for j in range(row,row+1-i-1,-1):
        print(chr(j),end= " ")
    print()
for i in range(1,row+1):
    for j in range(row+1 -i,row+1):
        print(chr(j+64), end =" ")
    print()
for i  in range(1,row+1):
    for j in range(i,1-1,-1):
        print(chr(j+64),end =" ")
    print()
for i in range(1,row+1):
    for j in range(1,row-i+1):
        print(" ",end =" ")
    for j in range(row+1-i,row+1):
        print("*",end = " ")
    print()

for i in range(1,row+1):
    for j in range(1,row-i+1):
        print(" ",end =" ")
    for j in range(row,row-i,-1):
        print(j,end = " ")
    print()
for i in range(1,row+1):
    for j in range(1,row-i+1):
        print(" ",end =" ")
    for j in range(i,0,-1):
        print(j,end = " ")
    print()