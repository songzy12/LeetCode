# when you guess a particular number x, and you guess wrong, you pay $x.
# You win the game when you guess the number I picked.
# Given a particular n >= 1, find out how much money you need to have to guarantee a win.

class Solution(object):
    def getMoneyAmount(self, n):
        """
        :type n: int
        :rtype: int
        """
        need = [[0] * (n+1) for _ in range(n+1)]
        for lo in range(n, 0, -1):
            for hi in range(lo+1, n+1):
                need[lo][hi] = min(x + max(need[lo][x-1], need[x+1][hi])
                                   for x in range(lo, hi))
        return need[1][n]

# the binary search method does not mean least money
# need to check for every possible guess path
# while use dp to memorize the reusable ones
