class Solution:
    def customSortString(self, S, T):
        """
        :type S: str
        :type T: str
        :rtype: str
        """
        order = {}
        for i, s in enumerate(S):
            order[s] = i

        T = list(T)
        T.sort(key=lambda x: order.get(x, -1))
        return ''.join(T)

S = "cba"
T = "abcd"
print(Solution().customSortString(S, T))
        
