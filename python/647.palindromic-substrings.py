class Solution(object):
    def countSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        def get_count_odd(i):
            c = 0
            while i + c < len(s) and i - c >= 0 and s[i+c] == s[i-c]:
                c += 1
            return c
        def get_count_even(i):
            c = 0
            while i+1+c < len(s) and i-c >= 0 and s[i+1+c] == s[i-c]:
                c += 1
            return c
        ans = 0 
        for i in range(len(s)):
            # a[i]
            # a[i], a[i+1]
            ans += get_count_odd(i) + get_count_even(i)
        return ans
            
