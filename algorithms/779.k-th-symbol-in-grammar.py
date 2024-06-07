# https://leetcode.com/problems/k-th-symbol-in-grammar/description/

class Solution:
    def kthGrammar(self, N, K):
        """
        :type N: int
        :type K: int
        :rtype: int
        """
        K -= 1
        if N == 1:
            return 0
        temp = self.kthGrammar(N-1, K//2 + 1)
        if temp == 0:
            return K % 2
        else:
            return 1 - (K % 2)

for N, K in [[1,1], [2,1], [2,2], [4,5]]:
    print(Solution().kthGrammar(N, K))
