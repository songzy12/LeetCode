class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        i, j, n = 0, 0, len(nums)
        while j < n:
            if nums[j]:
                nums[i] = nums[j]
                i += 1
            j += 1
        while i < n:
            nums[i] = 0
            i += 1
        return 

nums = [0,1,0,3,12]
print Solution().moveZeroes(nums)
        
