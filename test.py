# a, b = 0, 0

# arr1 = [1,2,3,None]
# arr2 = [1,2,3,4,5,6,None]

# while arr1[a] is not None or arr2[b] is not None:
#     if arr1[a] != None:
#         print(arr1[a])
#         a += 1
#     if arr2[b] != None:
#         print(arr2[b])  
#         b += 1

# a = 1
# b = None

# if a > b:
#     print(True)
# else:
#     print(False)
num = 50
arr = [1,2,3,4,5,6,7,8]
for i in range(len(arr) - 1, -1, -1):
    arr[i] = arr[i -1]
arr[0] = num
print(arr)