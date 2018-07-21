# https://leetcode.com/problemset/algorithms/?difficulty=Hard&status=Todo
# https://leetcode.com/problems/maximum-sum-of-3-non-overlapping-subarrays/description/


class Solution:

    def maxSumOfThreeSubarrays(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        sum_k = [0 for i in range(len(nums))]
        sum_k[0] = sum(nums[:k])
        for i in range(1, len(nums) - k):
            sum_k[i] = sum_k[i - 1] - nums[i - 1] + nums[i + k - 1]

        from collections import defaultdict
        dp = defaultdict(int)
        result = defaultdict(list)

        def get_dp(index, segment):
            if (index, segment) in dp:
                return dp[index, segment], result[index, segment]
            if len(nums) - index == k * segment:
                dp[index, segment] = sum(nums[index:])
                result[index, segment] = [
                    index + i * k for i in range(segment)]                
            elif segment == 1:
                temp_dp, temp_result = get_dp(index + 1, segment)
                if sum_k[index] < temp_dp:
                    dp[index, segment] = temp_dp
                    result[index, segment] = temp_result
                else:
                    dp[index, segment] = sum_k[index]
                    result[index, segment] = [index]
            else:

                temp_dp0, temp_result0 = get_dp(index + k, segment - 1)
                temp_dp1, temp_result1 = get_dp(index + 1, segment)
                if sum_k[index] + temp_dp0 < temp_dp1:
                    dp[index, segment] = temp_dp1
                    result[index, segment] = temp_result1
                else:
                    dp[index, segment] = sum_k[index] + temp_dp0
                    result[index, segment] = [index] + temp_result0
            return dp[index, segment], result[index, segment]
        dp, result = get_dp(0, 3)
        return result


nums = [7,13,20,19,19,2,10,1,1,19]
k = 3
print(Solution().maxSumOfThreeSubarrays(nums, k))

# dp[index][segment]：从 index 开始找出这样的 segment 段的和最大值
# 要求的结果就是 dp[0][3]
# dp[index][1] = max(sum(nums[index:index+k], dp[index+1][1])
# dp[index][segment] = max(sum(nums[index:index+k]) + dp[index+k][segment-1], dp[index+1][segment])
