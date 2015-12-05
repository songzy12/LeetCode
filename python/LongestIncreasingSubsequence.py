class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        dp = [1 for i in range(len(nums))]
        res = 1
        for i in range(len(nums)):
            # longest with last number i
            for j in range(i):
                if nums[j] < nums[i]:
                    # position of the number ahead of i
                    dp[i] = max(dp[i], dp[j] + 1)
            res = max(res, dp[i])
        return res

nums = [10, 9, 2, 5, 3, 7, 101, 18]
print Solution().lengthOfLIS(nums)
