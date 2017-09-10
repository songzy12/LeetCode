class Solution(object):
    def findLengthOfLCIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        ans = 1
        temp = 1
        for i in range(1, len(nums)):
            if nums[i] > nums[i-1]:
                temp += 1
            else:
                if temp > ans:
                    ans = temp
                temp = 1
        if temp > ans:
            ans = temp
        return ans

nums = [1,2,3,1,2,3,4,1,23]
print Solution().findLengthOfLCIS(nums)
