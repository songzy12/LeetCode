class Solution:
    def rotatedDigits(self, N):
        """
        :type N: int
        :rtype: int
        """
        
        def check(n):
            nums = set(str(n))
            if nums & set("347"):
                return False
            if not (nums & set("2569")):
                return False
            return True
            
        return sum([check(x) for x in range(1, N+1)])

N = 857
print(Solution().rotatedDigits(N))
