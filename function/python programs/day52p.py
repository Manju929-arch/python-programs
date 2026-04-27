# # arr = [ 10,20,30,40,50]
# # s = "hello"
# # s1= 'hello'
# # s2 = """hello
# #         hi"""
# # print(s1)
# # print(s2)
# # arr[0]=99
# # print(arr)
# # # s[0] = "s"
# # # print(s)
# # res = "s"+s[1:]
# # print(res)
# # print(s[0])
# # print(s[0:3])
# # print(s[-1])
# # print(s[::-1])
# #
# # for i in range(0,len(s)):
# #     print(s[i])
# #
# # print("***************************")
# # for ch in s:
# #     print(ch)
# # print("********************************")
# # for ch in s1:
# #     print(ch)
# if __name__ == '__main__':
#
#     s1 = input("Enter the string ")
#     res = ""
#     for i in range(len(s1)-1,-1,-1):
#         res = res+s1[i]
#     print(res)
#     res1 =""
#     # for i in range(0,len(s1)):
#     #     res1 = s1[i]+res1
#     if s1  == res:
#         print("it is palindrome")
#     else:
#         print("not a palindrome")
# #inbuilt string methods
#     u_str = s1.upper()
#     print(u_str)
#     l_str = s1.lower()
#     print(l_str)
#     swap = s1.swapcase()
#     print(swap)

if __name__ == '__main__':
    s = "hello"
    s1 = "1234"
    s3 = "hello123"
    print(s.isnumeric())
    print(s.isalpha())
    print(s.isalnum())
    print(s1.isnumeric())
    print(s1.isalpha())
    print(s1.isalpha())
    print(s3.isnumeric())
    print(s3.isalpha())
    print(s3.isalnum())





