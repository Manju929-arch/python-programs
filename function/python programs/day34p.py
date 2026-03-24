# for i in range(1,5+1):
#     for j in range(1,3+1):
#         if(i==1 or i==5 or j==1 or j==3):
#             print("*",end=" ")
#         else:
#             print(" ",end=" ")
#     print(" ", end=" ")
#     for j in range(1, 3 + 1):
#         if (j == 3):
#             print("*", end=" ")
#         else:
#             print(" ", end=" ")
#     print(" ", end=" ")
#     print("",end=" ")
#     for j in range(1,3+1):
#         if(i==1 or i==3 or i==5 or (j==1 and i>=3) or (j==3 and i<=3)):
#             print("*",end=" ")
#         else:
#             print(" ",end=" ")
#     print(" ", end=" ")
#     for j in range(1,3+1):
#         if(i==1 or i==3 or i==5 or (j==3 and i>=3) or (j==3 and i<=3)):
#             print("*",end=" ")
#         else:
#             print(" ",end=" ")
#     print(" ", end=" ")
#     for j in range(1,3+1):
#         if((j==1 and i<=3)or i==3 or j==3):
#             print("*",end=" ")
#         else:
#             print(" ",end=" ")
#     print(" ", end=" ")
#     for j in range(1,3+1):
#         if(i==1 or i==3 or i==5 or (j==1 and i<=3) or (j==3 and i>=3)):
#             print("*",end=" ")
#         else:
#             print(" ",end=" ")
#     print(" ", end=" ")
#     for j in range(1,3+1):
#         if(i==1 or i==3 or i==5  or j==1 or (j==3 and i>=3) ):
#             print("*",end=" ")
#         else:
#             print(" ",end=" ")
#     print(" ", end=" ")
#     for j in range(1,3+1):
#         if(i==1 or j==3 ):
#             print("*",end=" ")
#         else:
#             print(" ",end=" ")
#     print(" ", end=" ")
#     for j in range(1,3+1):
#         if(i==1 or i==5 or j==3 or j==1 or i==3 ):
#             print("*",end=" ")
#         else:
#             print(" ",end=" ")
#     print(" ", end=" ")
#     for j in range(1,3+1):
#         if(i==1 or i==5 or j==3 or (j==1 and i<=3) or i==3 ):
#             print("*",end=" ")
#         else:
#             print(" ",end=" ")
#     print(" ", end=" ")
#     for j in range(1,3+1):
#         if(j==3):
#             print("*",end=" ")
#         else:
#             print(" ",end=" ")
#     print(" ", end=" ")
#
#     for j in range(1,3+1):
#         if(i==1 or i==5 or j==3 or j==1  or  j==3):
#             print("*",end=" ")
#         else:
#             print(" ",end=" ")
#     print(" ", end=" ")
#     print()
#
#
#
# for i in range(1,5+1):
#
#     print()
#
#
# for i in range(1,5+1):
#
#     print()
#
#
# for i in range(1,5+1):
#
#     print()
#
# for i in range(1,5+1):
#
#     print()
#
# for i in range(1,5+1):
#
#     print()
#
# for i in range(1,5+1):
#
#     print()
#
# for i in range(1,5+1):
#
#     print()
#
#
# for i in range(1,5+1):
#
#     print()
# for i in range(1,5+1):
#
#     print()

for i in range(1,7):
    for j in range(1,8):
        if( j==1 or (i-j==0 and j<=4) or j==7 or (i+j==8 and j>=4) ):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print(" ",end=" ")
    for j in range(1,8):
        if j==1 or i==j+1 or (i==5 and j<4):
            print("*",end=" ")
        else:
            print(" ",end=" ")

    print()





