class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        l, r = 0, len(nums)-1
        while l != r:
            m = (l+r)//2
            if nums[m] < target:
                l = m + 1
            else:
                r = m
        if nums[l] != target:
            return [-1, -1]
        L, l, r = l, 0, len(nums)-1
        while l != r:
            m = (l+r)//2 + 1
            if nums[m] > target:
                r = m - 1
            else:
                l = m
        return [L, r]
        
nums = [1,2,8,8,9]
target = 10
print Solution().searchRange(nums, target)
