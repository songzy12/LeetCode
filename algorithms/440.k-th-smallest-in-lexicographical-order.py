class Solution(object):
    def findKthNumber(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: int
        """
        cur = 1
        k -= 1
        while k:
            steps = self.calc(n, cur, cur + 1)
            if steps <= k:
                cur += 1
                k -= steps
            else:
                cur *= 10
                k -= 1
        return cur
    
    def calc(self, n, n1, n2):
        steps = 0
        while n1 <= n:
            steps += min(n + 1, n2) - n1;
            n1 *= 10
            n2 *= 10
        return steps

# a denary tree
# simply add the number of nodes from n1 to n2 to steps.
