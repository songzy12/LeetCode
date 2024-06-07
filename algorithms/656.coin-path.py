class Solution(object):
    def cheapestJump(self, A, B):
        """
        :type A: List[int]
        :type B: int
        :rtype: List[int]
        """
        dp = [-1 for i in range(len(A))] # dp[i]: from i, the minimum cost
        steps = [[] for i in range(len(A))]
        N = len(A)
        def get_dp(i):
            if dp[i] != -1:
                return dp[i], steps[i]
            if i == N - 1:
                dp[i], steps[i] = A[i], []
                return dp[i], steps[i]
            cur_cost, cur_step = None, None
            for step in range(1, B+1):
                if i + step >= N or A[i+step] == -1: # index
                    continue
                temp_cost, temp_step = get_dp(i+step)

                #print i+step+1, temp_cost, temp_step

                if temp_cost == None:
                    continue
                if cur_cost == None or cur_cost > A[i+step]+temp_cost: # 
                    cur_cost, cur_step = A[i+step] + temp_cost, [i + step + 1] + temp_step
                    continue
                if cur_cost < A[i+step] + temp_cost:
                    continue
                if tuple(cur_step) > tuple([i+step+1]+temp_step):
                    cur_cost, cur_step = A[i+step] + temp_cost, [i + step + 1] + temp_step
            dp[i] = cur_cost 
            steps[i] = cur_step
            return dp[i], steps[i]

        cur_step = get_dp(0)[-1]
        if cur_step == None: # None or []
            return []
        return [1] + cur_step

A = [1,0,1]
B = 2
print Solution().cheapestJump(A, B)
        
