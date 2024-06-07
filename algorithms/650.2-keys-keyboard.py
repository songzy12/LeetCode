class Solution(object):

    

    def minSteps(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 1: # no need to copy
            return 0
        
        dp = {}

        def get_dp(cur, last, n):
            if n == 0:
                return 0
            if n < 0:
                return -1
            if (cur, last) in dp:
                return dp[(cur, last)]
            paste = get_dp(cur+last, last, n-last)+1
            copy = get_dp(cur+cur, cur, n-cur)+2
            if paste == 0 and copy == 1:
                return -1
            if paste == 0:
                dp[(cur,last)] = copy
            elif copy == 1:
                dp[(cur,last)] = paste
            else:
                dp[(cur,last)] = min(copy, paste)
            return dp[(cur,last)]

        return 1+get_dp(1, 1, n-1) # 1 extra copy
        
print Solution().minSteps(3)
