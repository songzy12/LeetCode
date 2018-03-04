class Solution:
    def preimageSizeFZF(self, K):
        """
        :type K: int
        :rtype: int
        """
        def check(n):
            cnt = 0
            while n:
                n //= 5
                cnt += n
            return cnt

        l = -1
        r = 5 * 10**9

        while r - l > 1:
            m = (r + l) // 2
            if check(m) < K:
                l = m
            elif check(m) >= K:
                r = m
        # now r >= K, l < K and r - l = 1
        
        left = l

        l = -1
        r = 5 * 10**9

        while r - l > 1:
            m = (r + l) // 2
            if check(m) <= K:
                l = m
            elif check(m) > K:
                r = m
        # now left <= K, r > K and r - l = 1

        right = l
        
        return right - left

K = 5
print(Solution().preimageSizeFZF(K))
            
