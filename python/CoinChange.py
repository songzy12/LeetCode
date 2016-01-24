class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        dp_ = [0] + [amount + 1 for i in range(amount)]
        for i in range(1, amount+1):
            for coin in coins:
                if coin <= i:
                    dp_[i] = min(dp_[i], dp_[i-coin]+1)
        return dp_[amount] if dp_[amount] < amount + 1 else -1
        
##        coins = filter(lambda x: x > 0, coins)
##        dp_ = [0] + [-1 for i in range(amount)]
##        def dp(amount):
##            # note the order
##            if amount < 0:
##                return None
##            if dp_[amount] != -1:
##                return dp_[amount]
##            seq = filter(lambda x: x != None, [dp(amount - i) for i in coins])
##            dp_[amount] = min(seq)+1 if seq else None
##            return dp_[amount]
##        ans = dp(amount)
##        return ans if ans != None else -1

coins = [181,79,206,169,487,319,262,162,420]
amount = 4409
print Solution().coinChange(coins, amount)
                
