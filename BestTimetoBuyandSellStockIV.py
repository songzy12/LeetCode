class Solution:
    # @param {integer} k
    # @param {integer[]} prices
    # @return {integer}
    def maxProfit(self, k, prices):
        length = len(prices)
        if 2*k >= length:
            profit = 0
            for i in range(len(prices)-1):
                if prices[i+1] > prices[i]:
                    profit += prices[i+1] - prices[i]
            return profit
        t = [[0 for j in range(length)] for i in range(k+1)]
        # t[i][j] is best profit for i transactions up to time j
        for i in range(1, k+1): # start from 1, else one row shifted
            tmpMax = -prices[0]
            for j in range(1, length):
                t[i][j] = max(t[i][j-1], prices[j] + tmpMax) # sell out at j?
                tmpMax = max(tmpMax, t[i-1][j-1] - prices[j]) # buy in at j?
        for i in t:
            print(i)
        return t[k][length-1]

import random
prices = [random.randint(0,10) for i in range(10)]
k = 2
prices = [3,3,5,0,0,3,1,4]
print(prices, Solution().maxProfit(k, prices))
