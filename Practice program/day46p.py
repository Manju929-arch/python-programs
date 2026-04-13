# # binary search
# def binarysearch(arr,key):
#     start = 0
#     end =   len(arr)-1
#     while start<=end:
#         mid = (start+end)//2
#         if arr[mid] == key:
#             return mid
#         elif key<arr[mid]:
#             end = mid-1
#         else:
#             start = mid+1
#     return -1
# if __name__ == '__main__':
#     arr = [2,4,6,8,12,24,32]
#     key = 67
#     print(binarysearch(arr,key))
# Bubble sort

# def bobble(arr):
#     for i in range(0,len(arr)):
#         for j in range(0,len(arr)-1):
#             if arr[j]>arr[j+1]:
#                 arr[j],arr[j+1]= arr[j+1],arr[j]
#     print(arr)
# if __name__ == '__main__':
#     arr =[32,19,21,7,3,2]
#     bobble(arr)


# def compare_arr(arr,brr):
#     if len(arr)!= len(brr):
#         return False
#     for i in range(len(arr)):
#         if arr[i] != brr[i]:
#             return False
#         else:
#             continue
#     return  False
# if __name__ == '__main__':
#     arr = [12,32,10,24,45]
#     brr = [12, 32, 10, 24, 45]
#     print(compare_arr(arr,brr))

# def compare(arr,brr):
#     for i in range(len(arr)):
#         if arr[i]!= brr[i]:
#             return False
#         else:
#             continue
#     return True
# if __name__ == '__main__':
#     arr = [12,10,15,20,30]
#     brr = [12,10,13,20,30]
#     print(compare(arr,brr))