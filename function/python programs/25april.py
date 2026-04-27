# def uppercase(s):
#     res = ""
#     for ch in s:
#         if ord(ch)>=96 and ord(ch)<=122:
#             res += chr(ord(ch)-32)
#         else:
#             res += ch
#
#     return(res)
# def Lowercase(s):
#     low = ""
#     for ch in s:
#         if ord(ch)>=65 and ord(ch)<=90:
#             low += chr(ord(ch)+32)
#         else:
#             low+=ch
#     return low
# if __name__ == '__main__':
#     s = input("Enter the word to be converted")
#     res = uppercase(s)
#     low = Lowercase(s)
#     print(res ,low)

# def swaps(s):
#     res = ""
#     for ch in s:
#         if ord(ch)>=97 and ord(ch)<=122:
#             res += chr(ord(ch)-32)
#         elif ch == ' ':
#             res+= ' '
#         else:
#             res += chr(ord(ch)+32)
#
#     return(res)
#
# if __name__ == '__main__':
#     s = input("Enter the word to be converted")
#     res =swaps(s)
#
#     print(res)

def vowel(s,):
    v_array = ['a', 'e', 'i', 'o', 'u']
    v_count = 0
    c_count = 0
    s_count = 0
    n_count = 0
    al_count =0
    for ch in s:
        if ch in v_array:
            v_count += 1
        elif ch == ' ':
            s_count+=1
        elif ch.isnumeric():
            n_count +=1
        elif ch.isalpha():
            al_count+=1
        else:
            c_count += 1
    return(v_count,c_count,s_count,n_count,al_count)
if __name__ == '__main__':
    s = input("Enter the letter to find the vowel and consonant count")
    v,c,s,n,al= vowel(s)
    print("the vowels are ",v,"\nthe consonant are ",c,"\nthe space are ",s,"\nthe number are ")






