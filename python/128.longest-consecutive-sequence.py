class Solution:
    # @param {integer[]} nums
    # @return {integer}
    def longestConsecutive(self, nums):
        m = {}
        for i in nums:
            m[i] = 1
        ans = 1
        for i in nums:
            if not m[i]:
                continue
            m[i] = 0
            count = 1
            l,r = i-1,i+1
            while m.get(l): # l in m and m[l] != 0
                m[l] = 0
                l -= 1
                count += 1
            while m.get(r):
                m[r] = 0
                r += 1
                count += 1
            ans = max(ans, count)
        return ans
        
nums = [100, 4, 200, 1, 3, 2]
print(Solution().longestConsecutive(nums))
