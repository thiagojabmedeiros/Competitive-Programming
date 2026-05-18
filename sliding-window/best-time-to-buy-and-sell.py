def maxProfit(prices):
    l, r = 0, 1
    maxP = 0
    while r < len(prices):
        if prices[l] < prices[r]:
            maxP = max(maxP, prices[r] - prices[l])
        if prices[l] > prices[r] and r + 1 < len(prices):
            l = r
        r += 1
    print(maxP)

prices = [10,1,5,6,7,1]
maxProfit(prices)