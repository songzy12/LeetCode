# https://leetcode.com/problems/k-similar-strings/description/


class Solution:

    def kSimilarity(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: int
        """


A = "ab"
B = "ba"
print(Solution().kSimilarity(A, B))

# 为什么觉得这个跟抽象代数有关系 2333

# 哎居然是用 BFS