class Solution(object):
    def minimumDeleteSum(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: int
        """
        dp = {}

        def get_dp(i, j):

            if (i, j) in dp:
                return dp[i, j]

            if i == len(s1) and j == len(s2):
                return 0

            if i == len(s1):
                dp[i,j] = ord(s2[j]) + get_dp(i, j + 1)
                return dp[i, j]
            if j == len(s2):
                dp[i,j] = ord(s1[i]) + get_dp(i + 1, j)
                return dp[i, j]

            if s1[i] == s2[j]:
                dp[i, j] = get_dp(i+1, j+1)
            else:
                dp[i, j] = min(ord(s2[j]) + get_dp(i, j + 1),
                               ord(s1[i]) + get_dp(i + 1, j))
            return dp[i, j]

        dp = [[0 for i in range(len(s2) + 1)] for j in range(len(s1) + 1)]
        s1 = map(ord, s1)
        s2 = map(ord, s2)
        for i in range(len(s1), -1, -1):
            for j in range(len(s2), -1, -1):
                if i == len(s1) and j == len(s2):
                    continue
                
                if i == len(s1):                    
                    dp[i][j] = dp[i][j+1] + s2[j]
                    continue
                if j == len(s2):
                    dp[i][j] = dp[i+1][j] + s1[i]
                    continue

                if s1[i] == s2[j]:
                    dp[i][j] = dp[i+1][j+1]
                else:
                    dp[i][j] = min(s2[j] + dp[i][j+1],
                                   s1[i] + dp[i+1][j])

        return dp[0][0]

s1 = "obccpykoilcageyevlxucgjyvbdomyqhejpcwmxhmqmqkaenshxzxlnicrtbjqrrqtekfqx"
s2 = "bwdydeoatefsmmpvmzzgkgjiqtzrusegeujimrdlqlqyxvgovibbdygyytpikhqsuovgplfrxdmseskvojvgrimktakckvaockwnyknsetekuuqmlwksvoysubojvrihlprcrkbdcsyuxsueeotaziioqeeyufzwpjigougvexxqpucdgplmbmovsqrchyrfwtyejkoptalpmyiesjbekedxabncejtsmlsgpiyrkenghuzyzwxrwvtozdvfgrglkbatpbfwhkruzkeswsvlloldzubvmzpuqmwpuyzdhbwgtkcekdgt"
print len(s1), len(s2)
print Solution().minimumDeleteSum(s1, s2)
                
                    
