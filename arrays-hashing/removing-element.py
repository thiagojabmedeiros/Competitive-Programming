def removeElement(nums, val):
    i = 0
    while i < len(nums):
        if nums[i] == val:
            nums[i] = "_"
            j = i
            while j + 1 < len(nums):
                nums[j] = nums[j+1]
                j += 1
            nums[j] = "_"
            i -= 1
        i += 1

    print(nums)

    k = 0
    for i in nums:
        if i == "_":
            break
        k += 1
    return k

nums = [0,1,2,2,3,0,4,2]
val = 2
print(removeElement(nums, val))