def trapWater(height):
    if not height: 
        return 0
    l, r = 0, len(height) - 1
    lMax, rMax = height[l], height[r]
    res = 0
    while l < r:
        if height[l] < height[r]:
            l += 1
            lMax = max(lMax, height[l])
            res += lMax - height[l]
        elif height[l] >= height[r]:
            r -= 1
            rMax = max(rMax, height[r])
            res += rMax - height[r]
        print(res)

arr = [0,2,0,3,1,0,1,3,2,1]
trapWater(arr)