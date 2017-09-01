# binary search the answer


class Solution(object):
    def findKthNumber(self, m, n, k):
        """
        :type m: int
        :type n: int
        :type k: int
        :rtype: int
        """
        if m > n:
            m, n = n, m

        # now m <= n

        def binary_search(l, r):

            def check(p):
                cnt = 0
                for i in range(1, min(p, m)+1):
                    cnt += min(n, p / i)
                return cnt < k
                    
            while l < r:
                p = (l + r) / 2
                if check(p):
                    l = p + 1
                else:
                    r = p
            return l
                    
        return binary_search(1, m * n)

m = 2
n = 3
k = 6
print Solution().findKthNumber(m, n, k)
        
    
