class Solution(object):
    def findNumberOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dp, longest = [[1, 1] for i in range(len(nums))], 1
        # reduce the space complexity
        for i, num in enumerate(nums):
            curr_longest, count = 1, 0
            for j in range(i):
                if nums[j] < num:
                    curr_longest = max(curr_longest, dp[j][0] + 1)
            for j in range(i):
                if dp[j][0] == curr_longest - 1 and nums[j] < num:
                    count += dp[j][1]
            dp[i] = [curr_longest, max(count, dp[i][1])]
            longest = max(curr_longest, longest)
        return sum([item[1] for item in dp if item[0] == longest])
    
##        if not nums:
##            return 0
##        
##        dp = {}
##        def get_dp(num, i):
##            if i == len(nums):
##                return 0, 1
##            if (num, i) in dp:
##                return dp[num, i]
##            if nums[i] <= num:
##                dp[num, i] = get_dp(num, i+1)
##                return dp[num, i]
##            temp1 = get_dp(nums[i], i+1)
##            temp2 = get_dp(num, i+1)
##            if temp1[0] + 1 > temp2[0]:
##                dp[num, i] = temp1[0] + 1, temp1[1]
##            elif temp1[0] + 1 < temp2[0]:
##                dp[num, i] = temp2
##            else:
##                dp[num, i] = temp2[0], temp1[1] + temp2[1]
##            return dp[num, i]
##        ans = get_dp(min(nums)-1, 0)
##        
##        return ans[-1]

nums = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
print Solution().findNumberOfLIS(nums)
