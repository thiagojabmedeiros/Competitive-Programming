def searchInsert(arr, target):
    l, r = 0, len(arr) -1
    while l <= r:
        mid = (l + r) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] > target:
            r = mid - 1
        else:
            l = mid + 1

    if arr[mid] > target:
        return mid
    else:
        return mid + 1
    
print(searchInsert([0,3,4,5,7,11,20], 9))