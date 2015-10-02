class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        i, j = 0, len(nums)-1
        while i < j:
            mid = (i+j) // 2
            if nums[j] < nums[mid]:
                i = mid + 1
            elif nums[j] > nums[mid]:
                j = mid
            else:
                if nums[i] == nums[j]:
                    i += 1
                    j -= 1
                else:
                    j = mid
        return nums[j]

nums = [4,5,6,7,0,1,2]
print Solution().findMin(nums)
