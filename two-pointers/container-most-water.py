def containerMostWater(arr):
    containers = {}
    maxC = 0
    for l in range(len(arr)):
        containers[l] = []
        for r in range(1, len(arr)):
            value = min(arr[r], arr[l]) * (abs(l - r))
            containers[l].append(value)
            maxC = max(maxC, value)
    print(containers)
    print(maxC)

containerMostWater([2,2,2])