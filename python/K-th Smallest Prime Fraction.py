# https://leetcode.com/problems/k-th-smallest-prime-fraction/description/
class Solution:
    def kthSmallestPrimeFraction(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: List[int]
        """
        import bisect
        l, r, N = 0, 1, len(A)
        while True:
            m = (l + r) / 2
            # border is the index of A[j] where A[i] / A[j] < m
            border = [bisect.bisect(A, A[i] / m) for i in range(N)]
            cur = sum(N - i for i in border)
            if cur > K:
                r = m
            elif cur < K:
                l = m
            else:
                # the elements in border are indices
                # border[i] is the index j of A[j] for element A[i], we find the max one
                return max([[A[i], A[j]] for i, j in enumerate(border) if j < N], key=lambda x: x[0] / x[1])

A = [1, 2, 3, 5]
K = 3
print(Solution().kthSmallestPrimeFraction(A, K))

# https://leetcode.com/problems/kth-smallest-element-in-a-sorted-matrix/description/
# https://leetcode.com/problems/find-k-th-smallest-pair-distance/description/
# https://en.wikipedia.org/wiki/Young_tableau

# https://leetcode.com/problems/kth-smallest-element-in-a-sorted-matrix/discuss/85170/on-from-paper-yes-orows
# https://leetcode.com/problems/k-th-smallest-prime-fraction/discuss/115819/Summary-of-solutions-for-problems-%22reducible%22-to-LeetCode-378

##>>> for i in range(5): print(~i)
##
##-1
##-2
##-3
##-4
##-5

##def kthSmallestPrimeFraction(self, A, K):
##    class Row(int):
##        def __getitem__(self, j):
##            return float(self) / A[~j], [int(self), A[~j]]
##    return self.kthSmallest(map(Row, A), K)[1]
