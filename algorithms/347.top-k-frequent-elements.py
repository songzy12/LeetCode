class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        bucket = [[] for i in range(len(nums)+1)]
        m = {}
        for num in nums:
            m[num] = m.get(num,0) + 1
        for num in m:
            bucket[m[num]] += num,
        res = []
        for i in range(len(bucket)-1,-1,-1):
            if bucket[i]:
                res += bucket[i][:min(len(bucket[i]), k-len(res))]
            if len(res) == k:
                break
        return res

nums = [1,1,2,2,3,3]
k = 2
print Solution().topKFrequent(nums, k)
        
