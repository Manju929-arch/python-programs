# #Using third variable
# # 1
# # 1 2
# # 1 3 3
# # 1 4 4 4
# # 1 5 5 5 5
#
row =5
for i  in range(1,row+1):
    k=1
    for j in range(1,i+1):
        print(k,end=" ")
        k+=1
    print()


# 5
# 5 4
# 5 4 3
# 5 4 3 2
# 5 4 3 2 1
row = 5
for i in range(1,row+1):
    k=row
    for j in range(1,i+1):
        print(k,end=" ")
        k-=1
    print()
# 5
# 4 5
# 3 4 5
# 2 3 4 5
# 1 2 3 4 5
for i in  range(1,row+1):
    k=row+1-i
    for j in range(1,i+1):
        print(k,end=" ")
        k+=1
    print()
# a
# b c
# d e f
# g h i j
# k l m n o
k=1
for i in  range(1,row+1):

    for j in range(1,i+1):
        print(chr(k+96),end=" ")
        k+=1
    print()
# 1
# 0 1
# 0 1 0
# 1 0 1 0
# 1 0 1 0 1  without using if else condition
k=1
for i in  range(1,row+1):

    for j in range(1,i+1):
        print(k%2,end=" ")

        k+=1
    print()
# 1
# 0 1
# 0 1 0
# 1 0 1 0
# 1 0 1 0 1  using if else condition
k=1
for i in range(1,row+1):
    for j in range(1,i+1):
        if k%2 == 0:
            print(0,end=" ")
        else:
            print(1,end=" ")
        k+=1
    print()

for i in range(1,row+1):
    for j in range(1,i+1):
        if k%2 == 0:
            print(0,end=" ")
        else:
            print(1,end=" ")
        k+=1
    print()
# 0
# 1 2
# 3 4 0
# 1 2 3 4
# 0 1 2 3 4  without using if else


k=0
for i in range(1,row+1):
    for j in range(1,i+1):
        print(k%5,end =" ")
        k+=1
    print()
# 0
# 1 2
# 3 4 0
# 1 2 3 4
# 0 1 2 3 4 with using if else



k=0
for i in range(1,row+1):
    for j in range(1,i+1):
        if k==5:
            k=0
        print(k,end=" ")
        k+=1
    print()





