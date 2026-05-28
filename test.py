nums = [1,2,3,4,5,6,7,4,5,4,8]
print(f"before removing four: {nums}")
for i in range(len(nums)):
    if nums[i] == 4:
        nums[i] = None
        j = i
        while j + 1 < len(nums):
            nums[j] = nums[j+1]
            j += 1
        nums[j] = None

print(f"after removing four: {nums}")