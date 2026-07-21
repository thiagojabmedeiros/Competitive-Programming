def getConcatenation(nums):
    ans = []
    x = 0
    for i in range(len(nums) * 2):
        if x == len(nums):
            x = 0
        ans.append(nums[x])
        x += 1
    return ans

nums = [1,2,3]
print(getConcatenation(nums))