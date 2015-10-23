from heapq import *

class MedianFinder:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.heaps = [], []

    def addNum(self, num):
        """
        Adds a num into the data structure.
        :type num: int
        :rtype: void
        """
        small, large = self.heaps
        # minimum heap by default
        heappush(small, -heappushpop(large, num)) # push to small
        if len(large) < len(small):
            heappush(large, -heappop(small)) # large has more

    def findMedian(self):
        """
        Returns the median of current data stream
        :rtype: float
        """
        small, large = self.heaps
        if len(large) > len(small):
            return float(large[0])
        return (large[0]-small[0]) / 2.0

# Your MedianFinder object will be instantiated and called as such:
mf = MedianFinder()
mf.addNum(1)
mf.addNum(2)
print mf.findMedian()

