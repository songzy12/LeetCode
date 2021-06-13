# https://leetcode.com/contest/weekly-contest-76/problems/minimum-swaps-to-make-sequences-increasing/

# dp(i, a, b): means from index i, and A[i:] larger than a, B[i:] larger than b

class Solution:
    def minSwap(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: int
        """
        dp = {}
        def get_dp(i, a, b):
            if i == len(A):
                return 0
            if (i, a, b) in dp:
                return dp[i, a, b]
            
            if a >= A[i] or b >= B[i]:
                dp[i, a, b] = 1 + get_dp(i+1, B[i], A[i])
            elif a >= B[i] or b >= A[i]:
                dp[i, a, b] = get_dp(i+1, A[i], B[i])
            else:
                dp[i, a, b] = min(1 + get_dp(i+1, B[i], A[i]), get_dp(i+1, A[i], B[i]))
            return dp[i, a, b]
        return min(get_dp(1, A[0], B[0]), 1 + get_dp(1, B[0], A[0]))        

A = [1, 3, 5, 4]
B = [1, 2, 3, 7]
print(Solution().minSwap(A, B))
