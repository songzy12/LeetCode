class Solution:
    # @param {integer[]} prices
    # @return {integer}
    def maxProfit(self, prices):
        # note the boundary
        if not prices:
            return 0
        result = 0
        curmin = prices[0]
        for i in range(len(prices)-1):
            if prices[i+1] >= prices[i]:
                continue
            result += prices[i]-curmin
            curmin = prices[i+1]
        result += prices[len(prices)-1]-curmin
        return result

print(Solution().maxProfit([2,4,1,3]))
