# https://leetcode.com/problems/4sum-ii/description/


import collections


class Solution:
    def fourSumCount(
        self, nums1: list[int], nums2: list[int], nums3: list[int], nums4: list[int]
    ) -> int:

        AB = collections.Counter(a + b for a in nums1 for b in nums2)
        CD = collections.Counter(c + d for c in nums3 for d in nums4)

        ans = 0
        for t in AB.keys():
            ans += AB[t] * CD[-t]
        return ans
