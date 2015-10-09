class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return
        l, r = 1, len(nums)-1
        while l != r:
            
            less = more = 0
            m = (l+r)//2
            
            for i in nums:
                if l <= i <= m:
                    less += 1
                elif m < i <= r:
                    more += 1
            if less > m - l + 1:
                r = m
            else:
                l = m+1
        return l

nums = [3,1,3,4,2]
print Solution().findDuplicate(nums)
        
