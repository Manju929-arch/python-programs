# # for i in range(1,5):
# #     print(i,end=" ")
# #     for j in range(1,i+1):
# #         print(j,end=" ")
# #     print()
# #
# #
# # for i in range(1,5):
# #     print(i,end="")
# #     for j in range (5,5-i,-1):
# #         print("*",end=" ")
# #     print()
#
# # row =5
# # for i in range(1,row+1):
# #     for j in range(5,5-i,-1):
# #        print(j,end=" ")
# #     print()
# # for i in range(1,row+1):
# #     for j in range(row,row+1-i-1,-1):
# #         print(j,end= " ")
# #     print()
#
# row =5
# for i in range(1,5):
#     for j in range(1,i+1):
#        print(" ",end=" ")
#     for j in range(5,i,-1):
#         print("*",end=" ")
#     print()
#
#
# for i in range(1,5):
#     for j in range(1,5):
#         if(i==3 and j==2):
#             print(" ",end=" ")
#         else:
#             print("*",end=" ")
#     print()
#

#     *
#    * *
#   * *
#  * * * *
# * * * * *
for i in range(1,5):
 for j in range(1,6-i):
     print(" ",end=" ")
 for j in range(1,i+1):
     print("*",end=" ")

 for j in range(2,i+1):
     print("*",end=" ")


 print()


