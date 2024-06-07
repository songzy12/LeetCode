class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if len(prices) < 2:
            return 0
        # buy[i] is the maxProfit for any sequence ends with buy
        buy = [0 for i in range(len(prices))]
        sell = [0 for i in range(len(prices))]
        rest = [0 for i in range(len(prices))]
        buy[0], sell[0], rest[0] = -prices[0], 0, 0
        for i in range(1, len(prices)):
            buy[i] = max(buy[i-1], rest[i-1] - prices[i])
            sell[i] = max(sell[i-1], buy[i-1] + prices[i])
            rest[i]= max(rest[i-1], buy[i-1], sell[i-1])    
        return sell[i]
    
prices = [1, 2, 3, 0, 2]
print Solution().maxProfit(prices)
