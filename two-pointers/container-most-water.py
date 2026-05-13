def containerMostWater(arr):
    l, r = 0, len(arr) - 1
    res = 0
    while l < r:
        area = min(arr[l], arr[r]) * abs(l-r)
        if arr[l] <= arr[r]:
            l += 1
        elif arr[l] > arr[r]:
            r -= 1
        res = max(res, area)
    print(res)

containerMostWater([2,2,2])