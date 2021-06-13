class Solution(object):
    def increasingTriplet(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        c1 = c2 = 1<<31-1
        for i in nums:
            if i <= c1:
                c1 = i
            elif i <= c2:
                c2 = i
            else:
                return True
        return False

nums = [5,1,5,5,2,5,4]
print Solution().increasingTriplet(nums)
