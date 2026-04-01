# def hcf(a,b):
#     hcf =1
#     for i in range(1,min(a,b)+1):
#         if a%i ==0 and b%i ==0:
#                 hcf =i
#     return hcf
#
# if __name__ == '__main__':
#     a = 12
#     b = 42
#     res = hcf(a,b)
#     print(res)
from math import factorial


# def hcf(a,b):
#
#     for i in range(max(a,b),(a*b)+1):
#         if i%a ==0 and i%b==0:
#             return i
#
#
#
# if __name__ == '__main__':
#     a = 5
#     b = 7
#     print(hcf(a,b))  output 35

# def factorial(n):
#     fact= 1
#     for i in range(1,n+1):
#         fact = fact*i
#     return fact
# def krish(num):
#     res=0
#     while num !=0:
#         rem = num %10
#         res = res+factorial(rem)
#         num = num//10
#     return res
# if __name__ == '__main__':
#     num = 144
#     res = krish(num)
#     if num == res:
#         print("It krishnamurthy number ")
#     else:
#         print("It not krishnamurthy number ")

