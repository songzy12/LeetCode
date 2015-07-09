class Solution:
    # @param {integer[]} prices
    # @return {integer}
    def maxProfit(self, prices):
        if len(prices)==0:
            return 0
        curmin = max(prices)
        maxpro = 0
        for i in prices:
            if i < curmin:
                curmin = i
            if i - curmin > maxpro:
                maxpro = i - curmin
        return maxpro
        
print(Solution().maxProfit([0]))
