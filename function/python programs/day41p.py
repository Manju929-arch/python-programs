# num = int(input("Enter number: "))
# temp = num
# digits = len(str(num))
# sum = 0
#
# while temp > 0:
#     digit = temp % 10
#     sum += digit ** digits
#     temp //= 10
#
# if sum == num:
#     print("Armstrong number")
# else:
#     print("Not Armstrong number")

# Happy number
# def sum_of_square(num):
#     res = 0
#     while  num !=0:
#         rem = num%10
#         res = (rem*rem)+res
#         num = num//10
#     return res
#
#
# if __name__ == '__main__':
#     num = 7
#     res = sum_of_square(num)
#     # print(res)
#     while res!=1 and res!=4:
#         res = sum_of_square(res)
#         # print(res)
#     if res == 1:
#         print("Happy number")
#     else:
#         print("Not happy number")

# #  problem 2
# def sum_of_digit(num):
#     res = 0
#     while num!=0:
#         rem = num%10
#         res = rem+res
#         num = num//10
#     return res
# if __name__ == '__main__':
#     N =14
#     res = sum_of_digit(N)
#     num = N+1
#     while sum_of_digit(N)*2 != sum_of_digit(num):
#         num+=1
#     print(num)

def sum_of_square(num):
    res = 0
    while  num !=0:
        rem = num%10
        res = (rem*rem)+res
        num = num//10
    return res


if __name__ == '__main__':
    num = 7
    res = sum_of_square(num)
    # print(res)
    while res!=1 and res!=4:
        res = sum_of_square(res)
        # print(res)
    if res == 1:
        print("Happy number")
    else:
        print("Not happy number")


