class Solution(object):
    def minMoves2(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # median = sorted(nums)[len(nums) / 2]
        # return sum(abs(num - median) for num in nums)

        nums.sort()
        return sum(nums[~i] - nums[i] for i in range(len(nums) / 2))
        
# goal is median, but no need to find the exact media
