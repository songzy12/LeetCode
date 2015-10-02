class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if not nums:
            return []
        nums.sort()
        ans = [nums[:]]
        while True:
            i = j = len(nums)-1
            while i > 0 and nums[i-1] >= nums[i]:
                i -= 1
            # nums[i-1] < nums[i] >= nums[i+1] >= ... >= nums[-1]
            if not i:
                break
            while j > i - 1 and nums[j] <= nums[i-1]:
                j -= 1
            # nums[j] > nums[i-1]
            nums[i-1], nums[j] = nums[j], nums[i-1]
            nums = nums[:i] + nums[i:][::-1]
            # nums[j], nums[-1] <= nums[-2] <= nums[i]
            ans += nums[:],
        return ans

nums = [1]
print Solution().permuteUnique(nums)
