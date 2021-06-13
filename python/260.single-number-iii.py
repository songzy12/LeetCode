class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        res = 0
        for num in nums:
            res ^= num
        bit = 1 # find one bit different
        while not bit & res:
            bit <<= 1
        num0 = num1 = 0
        for num in nums:
            if num & bit:
                num0 ^= num
            else:
                num1 ^= num
        return [num1, num0]
'''
        res = []
        m = {}
        for i in nums:
            if i not in m:
                m[i] = 1
            else:
                m[i] = 0
        for i in m:
            if m[i]:
                res += i,
        return res
'''

nums = [1, 2, 1, 3, 2, 5]
print Solution().singleNumber(nums)
