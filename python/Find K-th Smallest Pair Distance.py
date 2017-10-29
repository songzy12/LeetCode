from bisect import bisect
class Solution(object):
    def smallestDistancePair(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        nums.sort()

        def check0(t):
            cnt = 0
            for i in range(len(nums)):
                cnt += bisect(nums, nums[i] + t - 1) - i - 1
            # cnt is the number of distances < t
            # print 'check0', t, cnt
            if cnt >= k:
                return False
            return True

        def check1(t):
            cnt = 0
            for i in range(len(nums)):
                cnt += len(nums) - bisect(nums, nums[i] + t)
            # cnt is the number of distances > t
            # print 'check1', t, cnt
            if cnt >= len(nums) * (len(nums) - 1) / 2 - k:
                return False
            return True
                

        left = 0
        right = nums[-1] - nums[0]
        while left < right:
            mid = (left + right) / 2 + 1
            # print left, right, mid
            if check0(mid):
                left = mid
            else:
                right = mid - 1
                
        return right

nums = [1,3,1]
k = 1
print Solution().smallestDistancePair(nums, k)
