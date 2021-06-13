# There is a list of sorted integers from 1 to n.
# Starting from left to right,
# remove the first number and every other number afterward
# until you reach the end of the list.
# Find the last number that remains starting with a list of length n.


class Solution(object):
    def lastRemaining(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 1:
            return 1
        return (n / 2 - self.lastRemaining(n / 2) + 1) * 2
        


# first thought: use one number sequence to denote the index of left number
# you can compute the formal expression, or just write that into a program

# second thought: recursive fomular, a_2n = 2*(n - a_n + 1)
# clever me ^_^
