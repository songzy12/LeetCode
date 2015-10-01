class Solution(object):
    def containsNearbyAlmostDuplicate(self, nums, k, t):
        """
        :type nums: List[int]
        :type k: int
        :type t: int
        :rtype: bool
        """
        if k < 1 or t < 0:
            return False
        nums = map(lambda x: x+(1<<31), nums)
        m = {}
        for i in range(len(nums)):
            bucket = nums[i]//(t+1)
            if bucket in m or \
               bucket-1 in m and nums[i]-m[bucket-1] <= t or \
               bucket+1 in m and m[bucket+1]-nums[i] <= t:
                return True
            if len(m) >= k:
                last = nums[i-k]//(t+1) 
                m.pop(last) # only one
            m[bucket] = nums[i]
        return False

nums, k, t = [2,4], 1, 1
print Solution().containsNearbyAlmostDuplicate(nums, k, t)
