# using the for loop
# def reveser(num):
#     res =0
#     while num!=0:
#         rem = num%10
#         num = num//10
#         res = (res*10)+rem
#     return res
# if __name__ == '__main__':
#     count=0
#     for k in range(1,10000):
#         num= k
#         rev = reveser(num)
#         if num == rev:
#             print(num)
#             count+=1
#         if count == 50:
#             break


# def reveser(num):
#     res =0
#     while num!=0:
#         rem = num%10
#         num = num//10
#         res = (res*10)+rem
#     return res
# if __name__ == '__main__':
#     k=1
#     count=0
#
#     while(True):
#         num= k
#         rev = reveser(num)
#         if num == rev:
#             print(num)
#             count+=1
#         if count == 50:
#             break
#         k+=1

# def reveser(num):
#     res =0
#     while num!=0:
#         rem = num%10
#         num = num//10
#         res = (res*10)+rem
#     return res
# if __name__ == '__main__':
#     k=1
#     count=0
#
#     while(True):
#         num= k
#         rev = reveser(num)
#         if num == rev:
#             print(num)
#             count+=1
#         if count == 50:
#             break
#         k+=1

# WAP TO PRINT FIRST 50 PALINDROME NUMBER USING THE WHILE LOOP
# def reveser(num):
#     res =0
#     while num!=0:
#         rem = num%10
#         num = num//10
#         res = (res*10)+rem
#     return res
# if __name__ == '__main__':
#     k=1
#     count=0
#
#     while(True):
#         num= k
#         rev = reveser(num)
#         if num == rev:
#             print(num)
#             count+=1
#         if count == 50:
#             break
#         k+=1


# # WAP TO PRINT THE AVERAGE OF THE FIRST X PALINDROM NUMBER
# def reveser(num):
#     res =0
#     while num!=0:
#         rem = num%10
#         num = num//10
#         res = (res*10)+rem
#     return res
# if __name__ == '__main__':
#     count=0
#     sum =0
#     x = int(input("enter the number"))
#     for k in range(1,10000):
#         num= k
#         rev = reveser(num)
#         if num == rev:
#             sum+=num
#             count+=1
#         if count == 50:
#             print(sum/x)
#             break
# WAP TO PRINT THE NUMBER OF THE COUNT OF THE FACTORS
# def count_fact(x):
#     count =0
#     for i in range(1,x+1):
#         if x%i ==0:
#             print(i)
#             count+=1
#     return count
#
#
#
# if __name__ == '__main__':
#     x = int(input("enter the number "))
#     fact = count_fact(x)
# print("the number of the factorial is ",fact)

# CHECK WHETHER IT PRIME OR NOT
# def count_fact(x):
#     count =0
#     for i in range(1,x+1):
#         if x%i ==0:
#             print(i)
#             count+=1
#     return count
#
#
#
# if __name__ == '__main__':
#     x = int(input("enter the number "))
#     fact = count_fact(x)
#     if fact == 2:
#         print("it is prime")
#     else:
#         print("Not a prime")


def count_fact(x):
    count =0
    for i in range(1,x+1):
        if x%i ==0:

            count+=1
    return count



if __name__ == '__main__':
    for k in range(1,10000):
        x=k
        fact = count_fact(x)
        if fact == 2:
            print(x)

