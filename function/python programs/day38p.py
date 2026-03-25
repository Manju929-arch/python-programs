# def check_perfect(num):
#     sum =0
#     for i in range(1,num):
#         if num %i ==0:
#             sum+=i
#     return sum
# if __name__ == '__main__':
#     num =6
#     sum = check_perfect(num)
#     if sum == num:
#         print("perfect")
#     else:
#         print("not a perfect")
# # write a program reverse the given number  without using string function
# num = 12356789
# res = 0
# while num!=0:
#     rem = num %10
#     num = num//10
#     res = (res*10)+rem
# print(res)

# WAP A PROGRAM TO CHECK WHETHER THE GIVEN NUMBER IS PALINDROEM OR NOT
# def reverse(num):
#     res = 0
#     while num != 0:
#         rem = num % 10
#         num = num // 10
#         res = (res * 10) + rem
#
#     return res
# if __name__ == '__main__':
#     num = 1223
#     rev = reverse(num)
#     if rev == num:
#         print("it is palindrome")
#     else:
#         print("it is not a palindrome")

# WAP A PROGRAM TO PRINT ALL THE PALINDROEM NUMBERS B/W 1 TO 10000

def reverse(num):
    res =0
    while num!=0:
        rem = num%10
        res = (res*10)+rem
        num = num//10
    return res
if __name__ == '__main__':

    for k in range(1,10000):
        num = k
        rev = reverse(num)
        if rev == num:
            print(num)

# WAP TO PRINT ALL THE PERFECT NUMBER B/W ONE TO  10000

# def check_perfect(n):
#     sum = 0
#     for  i in range(1,n):
#         if n%i ==0:
#             sum+=i
#     return sum
# if __name__ == "__main__":
#     for k in range(1,10000):
#         num=k
#         sum = check_perfect(num)
#         if sum == num:
#             print(num)





