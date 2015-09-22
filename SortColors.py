class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        low, high, i = 0, len(nums)-1, 0
        while i <= high: # not i <= len(nums)-1
            if nums[i] < 1:
                nums[i], nums[low] = nums[low], nums[i]
                low += 1 
                i += 1 # since nums[i] = 0
            elif nums[i] > 1:
                nums[i], nums[high] = nums[high], nums[i]
                high -= 1 # since we do not know nums[i]
            else:
                i += 1
        return
    
##        n0 = n1 = n2 = 0
##        for i in nums:
##            if i == 0:
##                n0 += 1
##            elif i == 1:
##                n1 += 1
##            elif i == 2:
##                n2 += 1
##        for i in range(n0):
##            nums[i] = 0
##        for i in range(n0, n0+n1):
##            nums[i] = 1
##        for i in range(n0+n1, len(nums)):
##            nums[i] = 2
##        return

nums = [0,1,2,0,1,2]
Solution().sortColors(nums)
print nums
    
