# Given a non-empty array containing only positive integers, 
# find if the array can be partitioned into two subsets 
# such that the sum of elements in both subsets is equal

class Solution(object):
    def canPartition(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if sum(nums) % 2:
            return False
        goal = sum(nums) / 2
        nums.sort()
        return self.select(nums, goal)
    
    def select(self, nums, goal):
        if not goal:
            return True
        if not nums:
            return False
        dp = [False for i in range(goal + 1)]
        dp[0] = True
        for num in nums:
            for sum in range(goal, num - 1, -1):
                dp[sum] = dp[sum] or dp[sum - num]
        return dp[goal]

nums = [1, 2, 3, 5]
print Solution().canPartition(nums)

# find the sum of one set, 
# for each element decide whether included in that set
# TLE
# use dp[j] for whether we can get sum j, reduce to n^2 
# since we do not consider possible sum greater than goal