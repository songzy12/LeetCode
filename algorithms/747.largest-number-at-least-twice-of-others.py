# https://leetcode.com/contest/weekly-contest-64/problems/largest-number-at-least-twice-of-others/
class Solution:
    def dominantIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        index = -1
        large = None
        second = None
        for i, num in enumerate(nums):
            if large == None:
                large = num
                index = i
                continue
            if num >= large:
                second = large
                large = num
                index = i
                continue
            if second == None:
                second = num
                continue
            if num > second:
                second = num
        # NOTE:corner case
        if second == None:
            return index
        return -1 if large < 2 * second else index
