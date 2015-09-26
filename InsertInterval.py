# Definition for an interval.
class Interval(object):
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

class Solution(object):
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[Interval]
        :type newInterval: Interval
        :rtype: List[Interval]
        """
        i = 0
        while i < len(intervals) and intervals[i].end < newInterval.start:
            i += 1
        if i == len(intervals):# since [i]
            return intervals + [newInterval] 
        j = i
        while j < len(intervals) and intervals[j].start <= newInterval.end:
            j += 1
        if j == 0: # since [j-1]
            return [newInterval] + intervals 
        return intervals[:i] +\
               [Interval(min(intervals[i].start, newInterval.start),\
                        max(intervals[j-1].end, newInterval.end))] +\
               intervals[j:]
        
intervals = [Interval(1,5)]
newInterval = Interval(0,0)
res = Solution().insert(intervals, newInterval)
for i in res:
    print i.start, i.end
