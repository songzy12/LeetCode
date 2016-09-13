# F(k) = 0 * Bk[0] + 1 * Bk[1] + ... + (n-1) * Bk[n-1].
# Calculate the maximum value of F(0), F(1), ..., F(n-1). 

class Solution(object):
    def maxRotateFunction(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        best = candidate = sum([i * x for (i, x) in enumerate(A)])
        total = sum(A)
        for a in A[::-1]:
            # order matters
            candidate = candidate + total - a * len(A)
            best = max(candidate, best)
        return best
            

# use F(n) to get F(n+1): F(n+1)-F(n) = sum(A) - len(A) * A[-1]
