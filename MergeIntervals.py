# Definition for an interval.
class Interval(object):
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e
    

class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        intervals.sort(key = lambda x: x.start) # key: a function
        i, ans = 0, []
        while i < len(intervals):
            left = intervals[i].start
            right = intervals[i].end
            while i < len(intervals) and intervals[i].start <= right:
                right = max(right, intervals[i].end)
                i += 1
            ans += [left, right],
        return ans


intervals = [Interval(1,3),Interval(2,6), Interval(15,18), Interval(8,10)]
print Solution().merge(intervals)
