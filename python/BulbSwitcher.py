class Solution(object):
    def bulbSwitch(self, n):
        """
        :type n: int
        :rtype: int
        """
        # off at the begining, on at last
        # => toggled for odd times
        # => can be divided by odd numbers of 1, 2, ..., n
        # => there are odd number of dividers
        # => it is a perfect squred number
        from math import sqrt
        return int(sqrt(n))

print Solution().bulbSwitch(3)
