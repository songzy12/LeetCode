# https://leetcode.com/problems/permutation-sequence/description/

class Solution(object):
    def getPermutation(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        FACT = self.computeFactorials(n)

        nums = [i+1 for i in range(n)]

        permutation = self.getPermutationHelper(nums, k, FACT)

        return ''.join([str(i) for i in permutation])

    def getPermutationHelper(self, nums, k, fact):
        if len(nums) == 1:
            return nums

        t = fact[len(nums) - 1]

        q, r = divmod(k, t)
        if r == 0:
            q -= 1
            r = t
        return [nums[q]] + self.getPermutationHelper(nums[:q] + nums[q+1:], r, fact)

    def computeFactorials(self, n):
        fact = [1 for i in range(n+1)]
        for i in range(1, n+1):
            fact[i] = fact[i-1]*i
        return fact


if __name__ == '__main__':
    for i in range(1, 3*2*1 + 1):
        print(Solution().getPermutation(3, i))
