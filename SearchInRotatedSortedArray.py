class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        l, r = 0, len(nums)-1
        while l <= r:
            m = (l+r)//2
            if nums[m] == target:
                return m
            elif nums[m] > target:
                if nums[m] < nums[r]:
                    r = m - 1
                else:
                    if nums[r] < target:
                        r = m - 1
                    else:
                        l = m + 1
            else:
                # m == l
                if nums[m] >= nums[l]:
                    l = m + 1
                else:
                    if nums[l] > target:
                        l = m + 1
                    else:
                        r = m - 1
        return -1

nums = [1, 3]
target = 3
print Solution().search(nums, target)
