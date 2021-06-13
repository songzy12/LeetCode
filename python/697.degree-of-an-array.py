class Solution(object):
    def findShortestSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        from collections import Counter
        c = Counter(nums)
        max_value = max(c.values())
        max_keys = filter(lambda x: c[x] == max_value, c)
        # print max_keys

        index = {}
        for i, num in enumerate(nums):
            if num not in index:
                index[num] = [i, i]
            else:
                index[num][-1] = i

        ans = len(nums)
        for key in max_keys:
            temp = index[key][-1] - index[key][0] + 1
            if temp < ans:
                ans = temp
        return ans

nums =  []
print Solution().findShortestSubArray(nums)
            
