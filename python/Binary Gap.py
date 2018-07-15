class Solution(object):
    def binaryGap(self, N):
        """
        :type N: int
        :rtype: int
        """
        str_n = str(bin(N)[2:])
        
        ans = 0
        last = len(str_n)
        for i, c in enumerate(str_n):
            if c == '1':
                temp = i - last
                if temp > ans:
                    ans = temp
                last = i
        return ans

N = 22
print Solution().binaryGap(N)