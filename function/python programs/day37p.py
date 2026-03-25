# if __name__ == "__main__":
#     n = int(input("Enter the number"))
#     for i in range(1,n+1):
#         print(i)
# print("------------------------------------")
# for i in range(1,n+1):
#         if i%2==0:
#            print(i)
# print("-----------------------------------------")
# for i in range(1,n+1):
#         if i %2!=0:
#             print(i)


# if __name__ == "__main__":
#     n = 28
    # for i in range(1,n+1):
    #         if i%2!=0:
    #            print(i,end=" ")
    #         else:
    #             print(i)
    #     if i in range(1,12):
    #         if 12%i==0:
    #             print(i)
    # for i in range(12,10000):
    #     if i%12 ==0:
    #         print(i)
    #
    # for i in range(1,10000,12):
    #     print(i)
    #
    # for i in range(1,10):
    #     if i%2 !=0:
    #         print(i,end=" ")
    #     else:
    #         print(i)
    # sum=0
    # for i in range(1,n+1):
    #     sum+=i
    # print(sum)

    # sum=0
    # for i in range(1,n):
    #     if n % i ==0:
    #         sum+=i
    # if sum == n:
    #     print("perfect")
    # else:
    #     print("not a perfect")



def check_perfect(n):
    sum = 0
    for  i in range(1,n):
        if n%i ==0:
            sum+=i
    return sum
if __name__ == "__main__":
    n=27
    sum = check_perfect(n)
    if sum == n:
        print("perfect")
    else:
        print("not  perfect")










