def binarySearch(list, target):
    l, r = 0, len(list) - 1
    while l <= r:
        mid = (l + r) // 2
        if list[mid] == target:
            return mid
        elif list[mid] > target:
            r = mid - 1
        else:
            l = mid + 1
    return False

list = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]
print(binarySearch(list, 12))