# https://leetcode.com/problems/range-module/description/
# https://leetcode.com/problems/shortest-subarray-with-sum-at-least-k/


class Solution:

    def shortestSubarray(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: int
        """
        B = [0 for i in range(len(A) + 1)]
        for t in range(len(A)):
            B[t + 1] = B[t] + A[t]
        # B[t] = sum(A[:t])
        res = len(A) + 1
        d = []
        for i in range(len(A) + 1):
            while d and B[i] >= B[d[0]] + K:
                res = min(res, i - d.pop(0))
            while d and B[i] <= B[d[-1]]:
                d.pop(-1)
            d += [i]

        return -1 if res == len(A) + 1 else res


A = [48, 99, 37, 4, -31]
K = 140
print(Solution().shortestSubarray(A, K))

# 想法应该是一个 sliding window 吧

# 不是的，我能想出一个 n\log n 的解法：
# 计算前缀和 B, 然后对于每一个 B[i], 二分查找 B[i] + K
# 然后计算两个下标的差

# 不对的，因为二分查找的假设是 B 是排好序的，然而不是

# 只需要维持一个单增的前缀和数列就可以了
# 为什么要单增呢？
# 因为如果有递减，那么与后面的较小值作差，差值更大，长度更短
# 于是便不必要保存前面的值
