class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        cur = curMax = step = 0
        while cur < len(nums):
            if curMax >= len(nums)-1:
                return step
            tempMax = curMax
            while cur <= curMax:
                tempMax = max(tempMax, cur+nums[cur])
                cur += 1
            step += 1
            curMax = tempMax
        
    
##        dp = [1<<28 for i in range(len(nums))] # TLE
##        dp[-1] = 0
##        for i in range(len(nums)-2, -1, -1):
##            for j in range(1, nums[i]+1):
##                if i+j >= len(nums):
##                    break
##                dp[i] = min(dp[i], dp[i+j]+1)
##        return dp[0]
        
nums = [1,1,2,1,1]
print Solution().jump(nums)
