class Solution:
    def splitArraySameAverage(self, A):
        """
        :type A: List[int]
        :rtype: bool
        """
        # x + y = len(A)
        # ave * x + ave * y = sum(A)
        # ave = sum(A) / len(A)

        ave = sum(A) / len(A)
        len_A = len(A)
        sum_A = sum(A)
        prefix = [0]
        for a in A:
            prefix.append(prefix[-1] + a)
            
        def get_dp(index, i, sum_a):
            
            if index == len(A):
                return sum_a == 0 and i == 0

            if (index, i, sum_a) in dp:
                return dp[index, i, sum_a]

            if i == 0:
                return sum_a == 0

            if i == len_A - index:
                return sum_A - prefix[index] == sum_a
            
            if sum_a >= A[index] and get_dp(index+1, i-1, sum_a - A[index]):
                dp[index,i,sum_a] = True
                return True

            if get_dp(index+1, i, sum_a):
                dp[index, i, sum_a] = True
                return True
            
            dp[index, i, sum_a] = False
            return False

        dp = {}
            
        for i in range(0, len(A) // 2 + 1):
            if i == 0 and ave != 0:
                continue
            if int(i * ave) != i * ave: # NOTE: this is very important
                continue
            if get_dp(0, i, i * ave):
                return True
        return False
        

A = [18,10,5,3]
A = [3863,703,1799,327,3682,4330,3388,6187,5330,6572,938,6842,678,9837,8256,6886,2204,5262,6643,829,745,8755,3549,6627,1633,4290,7]
print(Solution().splitArraySameAverage(A))
