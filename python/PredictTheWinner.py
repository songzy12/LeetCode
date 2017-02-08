class Solution(object):
    def __init__(self):
        self.dp = {} # dp[(i,j)]: in nums[i:j] the gain of first player over second player

    def PredictTheWinner(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        return self.get(nums, 0, len(nums)) >= 0
     
    def get(self, nums, i, j):
        if (i,j) in self.dp :
            return self.dp[(i,j)]
        if i == j:
            return 0
        self.dp[(i,j)] = max(nums[i] - self.get(nums, i+1, j), nums[j-1] - self.get(nums, i, j-1))
        return self.dp[(i,j)]

# use dp, achieve n^2
