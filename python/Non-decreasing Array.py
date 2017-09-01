class Solution(object):
    def checkPossibility(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        cnt = 0
        for i in range(len(nums)-1):
            if nums[i] > nums[i+1]:
                cnt += 1
                if cnt > 1:                    
                    return False
                # [3,4,2,3]
                # [2,3,3,2,4]
                if i > 0 and nums[i-1] > nums[i+1] and \
                   i < len(nums) - 2 and nums[i+2]  < nums[i]:
                    return False
        return True

nums = [2,3,2,2,4]
print Solution().checkPossibility(nums)
