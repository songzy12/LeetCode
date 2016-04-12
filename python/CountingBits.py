class Solution(object):
    def countBits(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
        res = [0 for i in range(num+1)]
        for i in range(1, num + 1):
            res[i] = res[i-1] + 1 if i % 2 else res[i>>1]
        return res

print Solution().countBits(5)
            
