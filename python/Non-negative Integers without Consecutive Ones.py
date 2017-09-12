class Solution(object):
    
    def findIntegers(self, num):
        """
        :type num: int
        :rtype: int
        """
        num = bin(num)[2:]
        dp = [0 for i in range(len(num)+1)]
        
        dp[0] = 1
        dp[1] = 2
        for i in range(2, len(num)):
            dp[i] = dp[i-1] + dp[i-2]
        # print dp

        ans = dp[len(num)-1] # len 1: [0, 1]
        
        for i in range(1, len(num)):
            if num[i] == '0':
                continue
            if num[i] == '1':
                ans += dp[len(num) - 1 - i]
                if num[i-1] == '1':
                    break
        else:
            ans += 1 # if no break, then also count itself
        return ans
    

num = 10**9
print Solution().findIntegers(num)
