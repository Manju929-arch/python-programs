# # 1
# # 0 1
# # 1 0 1
# # 0 1 0 1
# # 1 0 1 0 1
#
# row = 5
#
# for i in range(1, row + 1):
#     k = i
#     for j in range(1, i + 1):
#         print(k%2, end=" ")
#         k -=1
#     print()
# # 0
# # 1 0
# # 0 1 0
# # 1 0 1 0
# # 0 1 0 1 0
# for i in range(1, row + 1):
#     k = i+1
#     for j in range(1, i + 1):
#         print(k%2, end=" ")
#         k-=1
#
#     print()
#
row = 5
k = 1

for i in range(1, row + 1):
    for j in range(1, i + 1):
        if k % 2 == 0:
            print(chr(k + 96), end=" ")
        else:
            print(chr(k + 64), end=" ")
        k += 1
    print()