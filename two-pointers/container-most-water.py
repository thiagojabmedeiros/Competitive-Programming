def containerMostWater(arr):
    containers = {}
    maxC = 0
    for l in range(len(arr)):
        containers[l] = []
        for r in range(1, len(arr)):
            if arr[l] == 1:
                containers[l] = [1] * (abs(l - r))
                maxC = max(maxC, 1)
                continue
            if arr[l] <= arr[r]:
                value = arr[l] * (abs(l - r))
                containers[l].append(value)
                maxC = max(maxC, value)
            
    print(containers)
    print(maxC)


containerMostWater([1,7,2,5,4,7,3,6])