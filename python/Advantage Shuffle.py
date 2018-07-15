class Solution(object):

    def advantageCount(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: List[int]
        """
        A = [(x, i) for i, x in enumerate(A)]
        B = [(x, i) for i, x in enumerate(B)]

        A.sort()
        B.sort()

        i = 0
        j = 0

        m = {}
        tail = []
        while i < len(A) and j < len(B):
            if A[i][0] > B[j][0]:
                m[B[j][1]] = A[i][0]
                i += 1
                j += 1

            else:
                tail.append(A[i][0])
                i += 1

        ans = []
        j = 0
        for i in range(len(B)):
            if i in m:
                ans.append(m[i])
            else:
                ans.append(tail[j])
                j += 1
        return ans


A = [2, 7, 11, 15]
B = [1, 10, 4, 11]

A = [12,24,8,32]
B = [13,25,32,11]
print Solution().advantageCount(A, B)
