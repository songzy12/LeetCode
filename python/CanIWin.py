# Given an integer maxChoosableInteger and another integer desiredTotal, 
# determine if the first player to move can force a win, 
# assuming both players play optimally. 

class Solution(object):
    def canIWin(self, maxChoosableInteger, desiredTotal):
        """
        :type maxChoosableInteger: int
        :type desiredTotal: int
        :rtype: bool
        """
        s = (1+maxChoosableInteger) * maxChoosableInteger / 2
        if s < desiredTotal:
            return False
        if desiredTotal <= 0:
            return True
        self.dp = {}
        self.used = [False] * (maxChoosableInteger + 1)
        return self.helper(desiredTotal)
    def helper(self, desiredTotal):
        # rather than check each unused > desired
        if desiredTotal <= 0:
            return False
        key = tuple(self.used) 
        if key in self.dp:
            return self.dp[key]
        for i in range(1, len(self.used)):
            if not i:
                continue
            if not self.used[i]:
                self.used[i] = True
                # opponent lose
                if not self.helper(desiredTotal - i):
                    self.dp[key] = True
                    self.used[i] = False
                    return True
                self.used[i] = False
        self.dp[key] = False
        return self.dp[key]

a = 20 
b = 210
print Solution().canIWin(a, b)
        
# state compression dp

# check each unused number one by one
# if all of them let next player win
# then I will lose
# if any of them let me win
# then I will win

# Is not there a math solution?
