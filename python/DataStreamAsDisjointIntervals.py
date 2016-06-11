# Definition for an interval.
class Interval(object):
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

import heapq
class SummaryRanges(object):

  def __init__(self):
    self.intervals = []

  def addNum(self, val):
    heapq.heappush(self.intervals, (val, Interval(val, val)))

  def getIntervals(self):
    stack = []
    while self.intervals:
        idx, cur = heapq.heappop(self.intervals)
        if not stack:
            stack.append((idx, cur))
        else:
            _, prev = stack[-1]
            if prev.end + 1 >= cur.start:
                prev.end = max(prev.end, cur.end)
            else:
                stack.append((idx, cur))
    self.intervals = stack
    return list(map(lambda x: x[1], stack))

# Your SummaryRanges object will be instantiated and called as such:
obj = SummaryRanges()
for val in  [1, 3, 7, 2, 6]:
    obj.addNum(val)
    print map(lambda x: [x.start, x.end], obj.getIntervals())
