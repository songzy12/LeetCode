# Given N axis-aligned rectangles where N > 0,
# determine if they all together form an exact cover of a rectangular region.
# Each rectangle is represented as a bottom-left point and a top-right point.

class Solution(object):
    def isRectangleCover(self, rectangles):
        """
        :type rectangles: List[List[int]]
        :rtype: bool
        """
        area = 0
        corners = set()
        a, c = lambda: (X - x) * (Y - y), lambda: {(x, y), (x, Y), (X, y), (X, Y)}
        for x, y, X, Y in rectangles:
            area += a()
            corners ^= c()
        x, y, X, Y = (f(z) for f, z in zip((min, min, max, max), zip(*rectangles)))
        return area == a() and corners == c()
        
# first thought: no thought, advanced data structure needed?
# the sum of areas matches the rectangular hull's area
# the corners appearing an odd number of times are exactly the hull's corners.
