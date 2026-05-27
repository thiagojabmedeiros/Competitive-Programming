def containsDuplicate(nums, k): 
    r = 0
    seen = {}
    while r < len(nums):
        if nums[r] in seen:
            print(r, seen[nums[r]])
            print(k, abs(seen[nums[r]] - r))
            return
        seen[nums[r]] = r
        r += 1

nums = [1,0,1,1]
containsDuplicate(nums, 2)