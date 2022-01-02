# https://leetcode.com/contest/weekly-contest-267/problems/time-needed-to-buy-tickets/


class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        res = 0
        h = tickets[k]
        for i, t in enumerate(tickets):
            if i <= k:
                res += min(h, t)
            else:
                res += min(h - 1, t)
        return res