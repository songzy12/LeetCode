class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return
        if nums[0] < nums[-1]:
            return nums[0]
        l, r = 0, len(nums)-1
        while l < r:
            m = (l+r)//2 # m is on the left, so compare with right
            if nums[m] > nums[r]:
                l = m + 1
            else:
                r = m
        return nums[l]

nums = [2,1]
print Solution().findMin(nums)
        
        
