class Solution(object):
    def countPalindromicSubsequences(self, S):
        """
        :type S: str
        :rtype: int
        """
        p = 10**9+7
        len_S = len(S)
        dp = {}
        # dp[i][j]: S[i:j+1]

        head = [[0 for i in range(len(S))] for j in range(4)]
        
        for index, c in enumerate('abcd'):
            stack = []
            i = 0
            while i < len(S):
                if S[i] == c:
                    while stack:
                        head[index][stack[-1]] = i
                        stack.pop(-1)
                    head[index][i] = i
                else:
                    stack += [i]
                i += 1
            while stack:
                head[index][stack[-1]] = i
                stack.pop(-1)

        tail = [[0 for i in range(len_S)] for j in range(4)]
        
        for index, c in enumerate('abcd'):
            stack = []
            i = len(S) - 1
            while i >= 0:
                if S[i] == c:
                    while stack:
                        tail[index][stack[-1]] = i
                        stack.pop(-1)
                    tail[index][i] = i
                else:
                    stack += [i]
                i -= 1
            while stack:
                tail[index][stack[-1]] = i
                stack.pop(-1)

        # print head, tail
        
        def get_dp(i, j):
            if (i, j) in dp:
                return dp[i, j]

            if i > j:
                return 0

            if i == j:
                return 1
            
            dp[i, j] = 0
            for index, c in enumerate('abcd'):
                head_ = head[index][i]
                tail_ = tail[index][j]

                # print head_, tail_
                if head_ > tail_:
                    continue
                
                dp[i, j] += 1
                if head_ == tail_:                    
                    continue
                dp[i, j] += 1 + get_dp(head_ + 1, tail_ - 1)
                dp[i, j] %= p
                
            return dp[i, j]
        
        return get_dp(0, len(S)-1)

S = "dacacddcdbdbcdbcbdaacbbdddbdbaabddaacdabcbaabadaaccdcddabcadacbcdabdaaccdbccbbccaabcbcbbdcccadababbddadbabcbdbddacccccbbcbbadbacaaccbbbaddcdbcacbaabbdbdbdbbadbcadbcadbcdbbaaadcddddddadacbacddcadbcbbddcacaddacddcbabdaddbbbdcdaaacdadabdbaabbbbadbccdbdbcbacbdcdddcbabdaabaddddabbbdcadccddcacccbabcbdcdabaabcccbbacadccbbbaabcababaccaaacddbcaaaacbbbbbdbbcacacbcaadadabdccbdbcbdbbbccbddabccbacaabacdddbccdddbdaacacdabaddbcacbaddbabcbaaddabdaddccadcdaacbadbcdccbaddbdabdbbddaccddadacdadcddacbbbbbcccbcaacabdabcbccdacbbdbaccaccadcdbcbccdcabbdaaacabdcadabbabdaadaaadcccddbabaccbddcddcbccdbbadaaaaaabbdccccadbacdadcaaacdcbbcbbcaadcccbabcddbdacbbcbbcaddabaabbcccdbccdbcabadbbbdcbcacdbadcadadddaabcdcddcdcaabaacbaccdacdaddcbdbdddaaccbbcdacaddaabbcdaabccbcdbccbbbaaaabdbabdcabbddcadcbadbbaccccbbccaadccbcdbabaaddcababbcccdabbdbaddbbccaaacdbbcdbdbcdaaacaaabccbdbcbabaadbcddaccaadccbcaacbbbaddadbabccacaccddababcdbdbadbbdcaadadbaccbbaddcdabadbbbdcabdccaadadbcbadccadabcdaadbabaabddcdbbcccabdccbbdcdbbbbbabdbbdbaaadb"
print Solution().countPalindromicSubsequences(S)
    

                    
                
