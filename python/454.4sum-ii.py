# Given four lists A, B, C, D of integer values,
# compute how many tuples (i, j, k, l) there are
# such that A[i] + B[j] + C[k] + D[l] is zero.

class Solution(object):
    def fourSumCount(self, A, B, C, D):
        """
        :type A: List[int]
        :type B: List[int]
        :type C: List[int]
        :type D: List[int]
        :rtype: int
        """
        import collections
        AB = collections.Counter(a+b for a in A for b in B)
        return sum(AB[-c-d] for c in C for d in D)
