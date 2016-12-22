class Solution(object):
    def totalHammingDistance(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count = [0 for i in range(32)]
        for num in nums:
            i = 0
            while num:
                count[i] += num & 1
                i += 1
                num >>= 1
        res = 0
        for t in count:
            res += t * (len(nums) - t)
        return res
            
nums = [4,14,4,14]
print Solution().totalHammingDistance(nums)
# expected 8
