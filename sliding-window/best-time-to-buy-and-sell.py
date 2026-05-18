def maxProfit(prices):
    maxP = 0
    for i in range(len(prices)):
        for j in range(i, len(prices)):
            maxP = max(maxP, prices[j] - prices[i])
    print(maxP)

prices = [10,1,5,6,7,1]
maxProfit(prices)