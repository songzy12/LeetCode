# Given a non-empty 2D matrix matrix and an integer k, find the max sum of a rectangle in the matrix such that its sum is no larger than k.

class Solution(object):
    def maxSumSubmatrix(self, matrix, k):
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """
        def maxSumSublist(vals):
            maxSum = float('-inf')
            prefixSum = 0
            prefixSums = [float('inf')]
            for val in vals:
                # insert x in a in sorted order.
                import bisect
                bisect.insort(prefixSums, prefixSum)
                prefixSum += val
                i = bisect.bisect_left(prefixSums, prefixSum - k)
                maxSum = max(maxSum, prefixSum - prefixSums[i])
            return maxSum
            
        maxSum = float('-inf')
        # If the form *identifier is present, it is initialized to a tuple receiving any excess positional parameters, defaulting to the empty tuple. 
        # If the form **identifier is present, it is initialized to a new dictionary receiving any excess keyword arguments, defaulting to a new empty dictionary.
        columns = zip(*matrix)
        for left in range(len(columns)):
            rowSums = [0] * len(matrix)
            for column in columns[left:]:
                rowSums = map(int.__add__, rowSums, column)
                maxSum = max(maxSum, maxSumSublist(rowSums))
        return maxSum              
    
matrix = [
  [1,  0, 1],
  [0, -2, 3]
]
k = 2

print Solution().maxSumSubmatrix(matrix, k)

