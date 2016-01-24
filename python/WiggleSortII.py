class Solution(object):
    def wiggleSort(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        nums.sort()
        # large half at odd indices
        length = (len(nums)+1) / 2
        # [4,5,5,6]
        nums[::2], nums[1::2] = nums[:length][::-1], nums[length:][::-1] 

nums = [1,2,2,3]
print nums
Solution().wiggleSort(nums)
print nums
