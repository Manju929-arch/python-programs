import math
from cmath import sqrt

# n= 24
# for i in range (1,n+1):
#     if n%i ==0:
#         print(i)
if __name__ == '__main__':
    n = 24
    for i in range(1, int(math.sqrt(n) + 1)):
        if n % i == 0:
            print(i)
    for i in range(int(math.sqrt(n)), 0, -1):
        if n % i == 0 and n/i != i:
            print(int(n / i))

def bobble(arr):
    for i in range(0,len(arr)):
        for j in range(0,len(arr)-1):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1]= arr[j+1],arr[j]
    print(arr)
if __name__ == '__main__':
    arr =[32,19,21,7,3,2]
    bobble(arr)