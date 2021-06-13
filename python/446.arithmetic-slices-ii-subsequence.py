# The function should return the number of arithmetic subsequence slices in the array A.

class Solution(object):
    def numberOfArithmeticSlices(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        res = 0
        m = [{} for i in range(len(A))]
        for i, x in enumerate(A):
            for j, y in enumerate(A[:i]):
                d = x - y
                c1 = m[i].get(d, 0)
                c2 = m[j].get(d, 0)
                res += c2
                m[i][d] = c1 + c2 + 1
        return res

# enumerate? cost time.
