class Solution(object):
    def largestPalindrome(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 1:
            return 9
        upper = 10**n - 1
        lower = upper / 10
        max_num = upper * upper 
        first_half = max_num / 10**n
        found = False
        while not found:
            palindrom = int(str(first_half)+str(first_half)[::-1]) 
            
            i = upper 
            while i > lower:
                if palindrom / i > max_num or i * i < palindrom:
                    break
                if palindrom % i == 0:
                    found = True
                    print i, palindrom / i, palindrom
                    break
                i -= 1
            first_half -= 1
        return palindrom % 1337

n = 8 
print Solution().largestPalindrome(n)
