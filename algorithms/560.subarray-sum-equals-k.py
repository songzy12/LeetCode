# https://leetcode.com/problems/subarray-sum-equals-k/description/

from collections import defaultdict
from typing import List


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix_sum_cnt = defaultdict(int)

        # Init for the empty prefix.
        prefix_sum = 0
        prefix_sum_cnt[prefix_sum] = 1

        ans = 0
        for num in nums:
            prefix_sum += num

            ans += prefix_sum_cnt[prefix_sum - k]
            prefix_sum_cnt[prefix_sum] += 1
        return ans


if __name__ == "__main__":
    nums = [-624, -624, -624, -624, -624, -624, -624, -624, -624, -624]
    k = -624

    print(Solution().subarraySum(nums, k))
