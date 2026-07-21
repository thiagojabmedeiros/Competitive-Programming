def findSmallestMissingPositive(orderNumbers):
    seen = {}
    minN = 1
    for i in range(len(orderNumbers)):
        if orderNumbers[i] < 1:
            continue
        minN = min(orderNumbers[i], minN)
        seen[orderNumbers[i]] = i
    if minN > 0:
        if minN not in seen:
            return minN
        while minN in seen:
            minN += 1
        return minN
    
nums = [3, 4, -1, 1]
print(findSmallestMissingPositive(nums))