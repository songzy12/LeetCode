class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        from collections import defaultdict
        m = defaultdict(int)
        
        sum_ = 0
        m[sum_] = 1
        count = 0
        for num in nums:
            sum_ += num
            count += m[sum_ - k]
            m[sum_] += 1
        return count

nums = [-624,-624,-624,-624,-624,-624,-624,-624,-624,-624]
k = -624

# prefix sum can reduce brute force O(n^3) to O(n^2)
# we can still use map to accelerate

# we need to index of sum t+k to be greater than t
# the key is to update the result during the computation
