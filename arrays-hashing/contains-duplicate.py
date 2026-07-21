def containsDuplicate(nums):
    seen = {}
    for i in range(len(nums)):
        if nums[i] in seen:
            return True
        seen[nums[i]] = i
    return False

nums = [1,2,3,4,5,5,1,2,2,3]

print(containsDuplicate(nums))