class Solution(object):
    def triangleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums = [x for x in nums if x] # x may be 0
        if len(nums) < 3:
            return 0
        nums.sort()
        from collections import Counter
        import bisect
        c = Counter(nums)
        
        ans = 0
        # 3 same        
        for k, v in c.items():
            if v >= 3:
                ans += v * (v-1) * (v-2) / 6
        
        # 2 same
        for k, v in c.items():
            if v >= 2:
                ans += v * (v-1) / 2 * (bisect.bisect_left(nums, 2 * k) - v)

        # no same
        c = [[k,v] for k,v in c.items()]
        c.sort() # sort
        for i in range(1, len(c)):
            c[i][1] += c[i-1][1]
        
        for i in range(len(c)):
            for j in range(i + 1, len(c)):
                index = bisect.bisect_left(c, [c[i][0] + c[j][0], 0])
                ans += (c[i][1]-(c[i-1][1] if i else 0))*(c[j][1]-c[j-1][1])*(c[index-1][1] - c[j][1])
        return ans

nums = [0,0,0]
print Solution().triangleNumber(nums)
