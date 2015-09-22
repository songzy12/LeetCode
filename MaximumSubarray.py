class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        tempSum, minSum, maxSum = nums[0], 0, nums[0]
        for i in nums[1:]:
            minSum = min(minSum, tempSum) # order matters
            tempSum += i
            maxSum = max(maxSum, tempSum - minSum)
        return maxSum
            
nums = [2, 1]
print Solution().maxSubArray(nums)
