def concatenation(nums):
    ans = []
    for i in range(2 * len(nums)):
        if i > len(nums) - 1:
            i -= len(nums)
        ans.append(nums[i])
    print(ans)
    
concatenation([1,2,3,4])