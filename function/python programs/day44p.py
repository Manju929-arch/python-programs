# # The max vlaue we are assuming
# l = [-23,-34,-9,-23,-31,-19]
# max_val = l[0]
# for i in range(0,len(l)):
#     curr_val = l[i]
#     if curr_val >max_val:
#         max_val = curr_val
# print(max_val)

# l= [12,23,34,45,56,67,78,89,]
# count =0
# sum =0
# for i in range(0,len(l)):
#     if l[i]%2 ==0:
#         sum+=l[i]
#         count+=1
# print(sum/count)

#
# l=[12,23,34,45,56,67,78,89]
# count =0
# sum =0
# for ele in l:
#     if ele%2 ==0:
#         sum+=ele
#         count+=1
# print(sum/count)

# if __name__ == '__main__':
def arrfuntion(l,key):


    for i in range(0,len(l)):
        if key==l[i]:
            return i

    return -1

if __name__ == '__main__':
    ke = int(input("Enter the key need to search"))
    l = [12, 23, 34, 45, 56, 67, 78, 89]
    print(arrfuntion(l,ke))


#method 2
if __name__ == '__main__':
    key = int(input("Enter the key need ot search"))
    l = [12, 23, 34, 45, 56, 67, 78, 89]
    index = -1
    for i in range(0,len(l)):
        if l[i]==key:
            index = i
        break
    print(index)









