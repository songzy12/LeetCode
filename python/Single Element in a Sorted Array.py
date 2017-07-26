class Solution(object):
    def singleNonDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l = 0
        r = len(nums) - 1
        while l < r:
            m = (l + r) / 2 # m may be the same as l
            # but m cannot be the same as l, since r - l = 0 or 2,4,6,...
            if nums[m-1] != nums[m] and nums[m+1] != nums[m]:
                return nums[m]
            if nums[m-1] == nums[m]:
                if (m - l + 1) % 2 == 0:
                    l = m + 1
                else:
                    r = m - 2
            elif nums[m+1] == nums[m]:
                if (m - l) % 2 == 0:
                    l = m + 2
                else:
                    r = m - 1
        return nums[l]
