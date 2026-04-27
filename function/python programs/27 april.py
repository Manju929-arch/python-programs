# def anagram(s1,s2):
#     s1.lower()
#     s2.lower()
#
#     if sorted(s1) == sorted(s2):
#         print("it is an anagram")
#     else:
#         print("not an anagram")
#
#
#
#
# if __name__ == '__main__':
#     s1  =input("Enter the word 1")
#     s2 = input("Enter the word 2")


# step 1 creaet sing  in ot chr
# fsor arr,brr using bubble sort
# comapre arr,brrr  using method


# def b_sort(arr):
#      for i in range(0,len(arr)):
#          for j in range(0,len(arr)-1):
#              if arr[j]>arr[j+1]:
#                 arr[j+1],arr[j] =arr[j]+arr[j+1]
#      return arr
# def compare_array(arr,brr):
#     if len(arr)!=0:
#         return False
#     for i in range(0,len(arr)):
#         if arr[i]!=arr[i+1]:
#             return False
#     return True
#
#
# if __name__ == '__main__':
#     s1 =  "silent"
#     s2 = "listen"
#     arr = []
#     for ch in s1:
#         arr.append(ch)
#     brr =[]
#     for  ch in s2:
#         brr.append(ch)
#     print(arr)
#     print(brr)
#     #after sorting
#     arr =b_sort(arr)
#     brr = b_sort(arr)
#     print(arr)
#     print(brr)
#     if compare_array(arr,brr):
#         print("it is anagaram")
#     else:
#         print("not a anagram")



