class Solution(object):
    def maxA(self, N):
        """
        :type N: int
        :rtype: int
        """

        dp = {}

        def get_dp(cur, last, n):
            if n < 0:
                return 0
            if n == 0:
                return cur
            if (cur, last, n) in dp:
                return dp[(cur,last,n)]

            if last > 0:
                temp1 = 0
            else:
                temp1 = get_dp(cur+1, last, n-1) # A    
            
            if n-3 >=0 and cur*2 > cur+last*3:
                temp3 = 0
            else:
                temp3 = get_dp(cur+last, last, n-1) # Ctrl-V 

            temp2 = get_dp(cur*2, cur, n-3) # Ctrl-A, Ctrl-C, Ctrl-V
            
            dp[(cur,last,n)] = max(temp1, temp2, temp3)
            return dp[(cur,last,n)]
        
        return get_dp(0, 0, N)

print Solution().maxA(45)
            
# MLE
