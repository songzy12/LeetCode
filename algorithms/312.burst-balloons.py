class Solution(object):
    def __init__(self):
        self.dp = []
        self.nums = []
        
    def maxCoins(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        self.nums = [1] + [i for i in nums if i > 0] + [1]
        n = len(self.nums)
        self.dp = [[-1]*n for _ in range(n)]
        return self.compute(0, n-1)
    
    def compute(self, left, right):
        if self.dp[left][right] != -1:
            return self.dp[left][right]
        if left == right - 1:
            self.dp[left][right] = 0
            return self.dp[left][right]
        # instead of divide the problem by the first balloon to burst,
        # we divide the problem by the last balloon to burst.
        for i in range(left+1, right):
            self.dp[left][right] = max(self.nums[left]*self.nums[i]*self.nums[right] +
                                       self.compute(left, i) + self.compute(i, right),
                                       self.dp[left][right])
        return self.dp[left][right]

nums = [3, 1, 5, 8]
print Solution().maxCoins(nums)
