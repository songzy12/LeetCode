class Solution:
    # @param {integer[]} prices
    # @return {integer}
    
##    def maxProfit(self, prices):
##        if not prices:
##            return 0
##        maxpro1, minind, maxind = self.auxMaxProfit(prices)
##        # can sell and buy at the same time
##        # if the first sell and last buy is between minind, maxind
##        # we can always adapt the first buy and last sell to minind, maxind
##        maxpro2 = max(self.auxMaxProfit(prices[:minind+1])[0],
##                     self.auxMaxProfit(prices[maxind:])[0],
##                     self.auxMaxProfit(prices[minind:maxind+1][::-1])[0])
##        maxpro = maxpro1 + maxpro2
##        return maxpro
##    
##    def auxMaxProfit(self, prices):
##        if not prices:
##            return 0, 0, 0
##        maxpro = 0
##        curmin = prices[0]
##        curminind = 0
##        minind = 0
##        maxind = 0
##        for i in range(len(prices)):
##            if prices[i]<curmin:
##                curmin = prices[i]
##                curminind = i
##            if prices[i]-curmin > maxpro:
##                maxpro = prices[i]-curmin
##                maxind = i
##                # notice minind and curminind
##                minind = curminind
##        return maxpro, minind, maxind
    def maxProfit(self, prices):
        hold1 = -2**31
        hold2 = -2**31
        release1 = 0
        release2 = 0
        for i in prices:
            release2 = max(release2, hold2 + i)
            hold2 = max(hold2, release1 - i)
            release1 = max(release1, hold1 + i)
            hold1 = max(hold1, -i)
        return release2

import random
prices = [random.randint(1,10) for i in range(10)]
print(prices)
print(Solution().maxProfit(prices))
