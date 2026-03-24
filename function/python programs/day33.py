  #  * * * * *
# #  * *   * *
# #  *   *   *
# #  * *   * *
# #  * * * * *
# Hallo printing of the star pattern No 1

row =9
for i  in range(1,row+1):
    for j in range(1,row+1):
        if i==1 or i==row or j==1 or j==row or i==j or row+1-i ==j :
            print("*",end=" ")
        else:
            print(" ",end=" ")

    print()

 # * * * * * * * * *
 # * *     *     * *
 # *   *   *   *   *
 # *     * * *     *
 # * * * * * * * * *
 # *     * * *     *
 # *   *   *   *   *
 # * *     *     * *
 # * * * * * * * * *
row =9
for i  in range(1,row+1):
    for j in range(1,row+1):
        if i==1 or i==row or j==1 or j==row or i==j or row+1-i ==j or (row+1)//2==i or (row+1)//2 ==j:
            print("*",end=" ")
        else:
            print(" ",end=" ")

    print()

  # 1 1 1 1 1 1 1 1 1
  # 2 2     2     2 2
  # 3   3   3   3   3
  # 4     4 4 4     4
  # 5 5 5 5 5 5 5 5 5
  # 6     6 6 6     6
  # 7   7   7   7   7
  # 8 8     8     8 8
  # 9 9 9 9 9 9 9 9 9
row =9
for i  in range(1,row+1):
    for j in range(1,row+1):
        if i==1 or i==row or j==1 or j==row or i==j or row+1-i ==j or (row+1)//2==i or (row+1)//2 ==j:
            print(i,end=" ")
        else:
            print(" ",end=" ")

    print()

  # 1 2 3 4 5 6 7 8 9
  # 1 2     5     8 9
  # 1   3   5   7   9
  # 1     4 5 6     9
  # 1 2 3 4 5 6 7 8 9
  # 1     4 5 6     9
  # 1   3   5   7   9
  # 1 2     5     8 9
  # 1 2 3 4 5 6 7 8 9


row =9
for i  in range(1,row+1):
    for j in range(1,row+1):
        if i==1 or i==row or j==1 or j==row or i==j or row+1-i ==j or (row+1)//2==i or (row+1)//2 ==j:
            print(j,end=" ")
        else:
            print(" ",end=" ")

    print()

  # 1 2 3 4 5 6 7 8 9
  #   2             9
  #     3           9
  #       4         9
  #         5       9
  #           6     9
  #             7   9
  #               8 9
  #                 9

row =9
for i  in range(1,row+1):
    for j in range(1,row+1):
        if i==1 or j==row or i==j  :
            print(j,end=" ")
        else:
            print(" ",end=" ")

    print()

# for i in range(6):
#     for j in range(7):
#         if(i==0 and j%3!=0) or (i==1 and j%3==0) or (i-j==2) or (i+j==8):
#             print("*",end=" ")
#         else:
#             print(" ",end=" ")
#     print()

for i in range(6):
    for j in range(7):
      if (i==1 and j%3==0) or (i==0 and j%3!=0) or (i-j ==2) or (i+j ==8):
          print("*",end=" ")
      elif i==2 and j==2:
          print("R",end=" ")
      elif i==2 and j==3:
          print("C",end=" ")
      elif i==2 and j==4:
          print("B",end=" ")
      else:
          print(" ",end=" ")
    print()
for i in range(6,0,-1):
    for j in range(7,-1):
      if (i==1 and j%3==0) or (i==0 and j%3!=0) or (i-j ==2) or (i+j ==8):
          print("*",end=" ")
      elif i==2 and j==2:
          print("R",end=" ")
      elif i==2 and j==3:
          print("C",end=" ")
      elif i==2 and j==4:
          print("B",end=" ")
      else:
          print(" ",end=" ")
    print()















