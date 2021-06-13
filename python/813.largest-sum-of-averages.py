class Solution:
    def largestSumOfAverages(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: float
        """
        dp = {}
        len_A = len(A)
        suffix_sum = [0]

        for a in A[::-1]:
            suffix_sum = [suffix_sum[0] + a] + suffix_sum
        
        def get_sum(index):
            return suffix_sum[index]
        
        def get_dp(index, k):
            if (index, k) in dp:
                return dp[index, k]
            if index == len_A:
                
                dp[index, k] = 0
                return dp[index, k]
            if k == 1:
                dp[index, k] = get_sum(index) / (len_A - index)
                return dp[index, k]
            ans = 0
            for t in range(index+1, len_A):
                temp = (suffix_sum[index] - suffix_sum[t]) / (t - index) + get_dp(t, k - 1)
                
                if temp > ans:
                    ans = temp
            dp[index,k] = ans
            return dp[index, k]
        
        return get_dp(0, K)
             

A = [9,1,2,3,9]
K = 3
print (Solution().largestSumOfAverages(A, K))
