class Solution(object):
    def __init__(self):
        self.nums = []
        self.dp = []
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        self.nums = nums
        self.dp = [-1 for i in range(len(nums))]
        val1 = nums[0]+self.robHelper(2, len(nums)-2)
        self.dp = [-1 for i in range(len(nums))]
        val2 = self.robHelper(1, len(nums)-1)
        return max(val1, val2)
    def robHelper(self, i, j):
        if i > j or i >= len(self.nums) or j < 0:
            return 0
        if self.dp[i] != -1:
            return self.dp[i]
        if i == j:
            self.dp[i] = self.nums[i]
            return self.dp[i]
        self.dp[i] = max(self.nums[i]+self.robHelper(i+2, j), self.robHelper(i+1, j))
        return self.dp[i]
        
nums = [11, 5, 3, 6]
print Solution().rob(nums)
