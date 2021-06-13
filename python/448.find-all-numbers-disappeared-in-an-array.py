class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        for num in nums:
            nums[abs(num)-1] = - abs(nums[abs(num)-1])
        return [i+1 for i, num in enumerate(nums) if num > 0]
        
# mark the index of what we have seen to -1
