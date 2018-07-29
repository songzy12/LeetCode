class Solution:

    def stoneGame(self, piles):
        """
        :type piles: List[int]
        :rtype: bool
        """

        prefix = [0 for i in range(len(piles) + 1)]
        for i in range(len(piles)):
            prefix[i + 1] = prefix[i] + piles[i]
        # prefix[i] = sum(piles[:i])

        def get_sum(i, j):
            return prefix[j + 1] - prefix[i]

        dp = {}

        def get_dp(i, j):
            if (i, j) in dp:
                return dp[i, j]
            if i == j:
                dp[i, j] = piles[i]
            else:
                dp[i, j] = max(piles[i] + get_sum(i + 1, j) - get_dp(i + 1, j),
                               piles[j] + get_sum(i, j - 1) - get_dp(i, j - 1))
            return dp[i, j]

        return get_dp(0, len(piles) - 1) > get_sum(0, len(piles) - 1) // 2

piles = [5,13,12,7]
print(Solution().stoneGame(piles))
