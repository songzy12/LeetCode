#  Given a positive integer n and you can do operations as follow:
#    If n is even, replace n with n/2.
#    If n is odd, you can replace n with either n + 1 or n - 1.
# What is the minimum number of replacements needed for n to become 1? 

class Solution(object):
    def integerReplacement(self, n):
        """
        :type n: int
        :rtype: int
        """
        ans = 0
        while n != 1:
            if n & 1:
                if n & 0x2 and n != 3:
                    n += 1
                else:
                    n -= 1
                ans += 1
            n >>= 1
            ans += 1
        return ans

#  you should create as many trailing zeroes as you can.
# This way you can avoid the tie-breaking trap (there can be no ties),
# but you'll still have to handle the n=3 exception separately.
