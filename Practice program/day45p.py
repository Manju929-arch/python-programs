# def anti_clock(arr):
#     temp = arr[0]
#     for i in range(1,len(arr)):
#         arr[i-1]= arr[i]
#     arr[len(arr)-1] = temp
# if __name__ == '__main__':
#     arr = [2,4,6,8,10,12]
#     anti_clock(arr)

# def anti_clock(arr):
#     temp = arr[0]
#     for i in range(1,len(arr)):
#         arr[i-1] = arr[i]
#     arr[len(arr)-1] = temp
#
# if __name__ == '__main__':
#     arr = [2,4,6,8,10,12]
#     for  i in range(4003%len(arr)):
#         anti_clock(arr)
#     print(arr)

def clock(arr):
    temp = arr[len(arr)-1]
    for i in range(len(arr)-2,-1,-1):
        arr[i+1]= arr[i]
    arr[0] = temp
    print(arr)

if __name__ == '__main__':
    arr = [2,4,6,8,10,12]
    for i in range( 4003%len(arr)):
        clock(arr)





