class Solution(object):
    def maximumProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        pos = [x for x in nums if x > 0]
        neg = [x for x in nums if x < 0]

        res = nums[-1] * nums[-2] * nums[-3] # 3 positive
        if len(pos) and len(neg) > 1:
            res = max(res, pos[-1] * neg[0] * neg[1]) # 1 postive
        if len(pos) > 1 and len(neg):
            res = max(res, pos[0] * pos[1] * neg[-1]) # 2 positive
        if 0 in nums:
            res = max(res, 0)
        if len(neg) > 2:
            res = max(res, neg[-1] * neg[-2] * neg[-3]) # 0 positive
        return res

nums = [-1,-2,-3, 1,2,3]
print Solution().maximumProduct(nums)
