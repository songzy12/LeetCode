class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: bool
        """
        if not nums:
            return False
        l, r = 0, len(nums)-1
        while l < r:
            m = (l+r)//2
            if nums[m] == target:
                return True
            if nums[m] > nums[r]:
                # compare nums[m] and nums[r]
                if nums[m] > target and nums[l] <= target:
                    r = m
                else:
                    l = m + 1
            elif nums[m] < nums[r]:
                if nums[m] < target and nums[r] >= target:
                    l = m + 1
                else:
                    r = m
            else:
                r -= 1
        return True if nums[l] == target else False

nums = []
target = 2
print Solution().search(nums, target)
