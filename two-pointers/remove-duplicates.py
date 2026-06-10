def removeDuplicates(nums: list):
    l, r = 0, len(nums)
    sNums = set()
    while l < r:
        if nums[l] in sNums:
            nums.pop(l)
            r -= 1
        else:
            sNums.add(nums[l])
            l += 1
    return len(nums)

val = removeDuplicates([1,3,4,5,6,1,1,3,8,9,10])
print(val)