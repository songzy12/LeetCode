class Solution(object):
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return -2147483648
        if len(nums) < 3:
            return max(nums)
        a, b, c = sorted(nums[:3])
        for i in nums[3:]:
            if i in [a, b, c]:
                continue
            if i > c:
                a, b, c = b, c, i
            elif i > b:
                a, b = b, i
            elif i > a:
                a = i
        return a
        
nums = [1, 2, 3, 4, 5]            
print Solution().thirdMax(nums)

