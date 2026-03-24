if __name__ == "__main__":

    # for i in range(1,row+1):
    #     for j in range(row,0,-1):
    #         print(j,end="")
    #     print()
    row = 5
    for i in range(1,row+1):
        for j in range(1,i+1):
            print("*",end="")
        print()
    row = 5
    for i in range(1,row+1):
        for j in range(1,i+1):
            print(i,end="")
        print()
    row = 5
    for i in range(1,row+1):
        for j in range(1,i+1):
            print( j,end=" ")
    print()
    row = 5
    for i in range(1,row+1):
        for j in range(row,row+1-i-1,-1):
            print(j,end=" ")
    print()
    row = 5
    for i in range(1, row + 1):
        for j in range(i,i+1):
            print(j, end=" ")
    print()
    for i in range(1, row + 1):
        for j in range(row,row-i,-1):
            print(j, end=" ")
    print()
    for i in range(1, row + 1):
        for j in range(row+i-1,row+1):
            print(j, end=" ")
    




