class Solution(object):

    def reorderedPowerOf2(self, N):
        """
        :type N: int
        :rtype: bool
        """

        import math
        temp = 1
        temp = 2 ** int(math.log(10**(len(str(N))-1), 2))
        
        def check(m, n):
            import string
            for t in string.digits:
                if str(m).count(t) != str(n).count(t):
                    return False
            return True

        while len(str(temp)) <= len(str(N)):
            if check(temp, N):
                return True
            temp *= 2

        return False

N = 1
print Solution().reorderedPowerOf2(N)