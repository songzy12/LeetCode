class Solution(object):
    def numberOfArithmeticSlices(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        if len(A) < 3:
            return 0
        d = A[1] - A[0]
        count = 2
        res = 0
        for i in range(2, len(A)):
            if A[i] - A[i-1] == d:
                count += 1
            else:
                d = A[i] - A[i-1]
                res += (count-2)*(count-1)/2
                count = 2
        res += (count-2)*(count-1)/2
        return res        

A = [1, 2, 3, 4]
print Solution().numberOfArithmeticSlices(A)
