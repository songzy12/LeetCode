class Solution:
    # @param {integer} s
    # @param {integer[]} nums
    # @return {integer}
    def minSubArrayLen(self, s, nums):
        # loop for the right end index of subarray
        # sub from left, rather than add from right
        l = r = total = 0
        while total < s:
            if r == len(nums):
                return 0
            total += nums[r]
            r += 1
        ans = r
        while True:
            if total >= s:
                while total >= s:
                    total -= nums[l]
                    l += 1
                temp = r - l + 1
                # print l, r, temp
                ans = min(temp, ans)
            if r == len(nums):
                break
            total += nums[r]
            r += 1
        return ans
    
s = 7
nums = [1,2,7,3,4]
print(Solution().minSubArrayLen(s, nums))
