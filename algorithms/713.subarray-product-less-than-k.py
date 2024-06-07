class Solution(object):
    def numSubarrayProductLessThanK(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """

        if not nums:
            return 0

        head = 0
        while head < len(nums) and nums[head] >= k:
            head += 1

        if head == len(nums):
            return 0

        prod = nums[head]
        ans = 1
        
        for tail in range(head + 1, len(nums)):
            while head < tail and nums[tail] * prod >= k:
                prod /= nums[head]
                head += 1
            prod *= nums[tail]
            tail += 1
            ans += tail - head

        return ans

nums, k = [1,1,1], 1
print Solution().numSubarrayProductLessThanK(nums, k)
                
            
            
