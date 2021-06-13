class Solution:
    # @param s, a string
    # @return a boolean
    def isPalindrome(self, s):
        # lambda, filter, list, str.isalnum, str.lower, reversed, join
        s=list(filter(lambda x: x.isalnum(),s.lower()))
        return ''.join(s)==''.join(reversed(s))

for s in ('1a2',''):
    print(Solution().isPalindrome(s))
