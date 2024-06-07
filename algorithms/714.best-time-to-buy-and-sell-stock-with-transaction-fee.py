class Solution(object):
    def maxProfit(self, prices, fee):
        """
        :type prices: List[int]
        :type fee: int
        :rtype: int
        """
        buy = [-1<<31 for i in range(len(prices)+1)]
        sell = [0 for i in range(len(prices)+1)]
        
        for i in range(len(prices)):
            buy[i+1] = max(sell[i] - prices[i], buy[i])
            sell[i+1] = max(buy[i+1] + prices[i] - fee, sell[i])

        return sell[-1]

prices = [1, 3, 2, 8, 4, 9]
fee = 2
print Solution().maxProfit(prices, fee)
