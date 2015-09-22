class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        from heapq import heappush, heappop
        data = []
        for i in nums[:k]:
            # heappush(data, -i)
            # return -data[0]
            heappush(data, i)
        for i in nums[k:]:
            heappush(data, i)
            heappop(data)
        return data[0]

nums = [1,2,3,4,5,6]
k = 4
print Solution().findKthLargest(nums, k)
        
