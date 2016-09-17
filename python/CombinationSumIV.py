# Given an integer array with all positive numbers and no duplicates,
# find the number of possible combinations that add up to a positive integer target.

class Solution(object):
    def combinationSum4(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        result = [0] * (target + 1)
        result[0] = 1
        for i in range(1, target + 1):
            for x in nums:
                if i >= x:
                    result[i] += result[i - x]
        return result[target]
        
# first thought: knapsack?
# simple dp
