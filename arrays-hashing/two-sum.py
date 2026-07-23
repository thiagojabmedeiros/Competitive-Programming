def twoSum(nums, target):
    seen = {}
    for i in range(len(nums)):
        complement = target - nums[i]
        if complement in seen:
            print(seen[complement], i)
        else:
            seen[nums[i]] = i
    return None

nums = [2,7,11,15]
target = 9
twoSum(nums, target)