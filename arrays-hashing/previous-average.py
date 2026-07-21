def countResponseTimeRegressions(responseTimes):
    if len(responseTimes) <= 1:
        return 0
    x = 0
    size = 0
    count = 0
    for i in range(len(responseTimes)):
        x += responseTimes[i]
        size += 1
        if i == 0:
            continue
        if responseTimes[i] > x // size:
            count += 1
    print(count)

nums = [100, 200, 300, 150, 220]
countResponseTimeRegressions(nums)