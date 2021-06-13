# https://leetcode.com/problems/range-module/description/
# https://leetcode.com/problemset/algorithms/?difficulty=Hard&status=Todo


class RangeModule:

    def __init__(self):

    def addRange(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: void
        """

    def queryRange(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: bool
        """

    def removeRange(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: void
        """


# Your RangeModule object will be instantiated and called as such:


obj = RangeModule()
obj.addRange(10, 20)
obj.removeRange(14, 16)
param_2 = obj.queryRange(10, 14)

# 拆分的时候怎么拆分呢
# 就像树的旋转一样？右边的那段作为右子树

# 区间树是这样的：查询一个区间和给定的区间组有没有交叉

# Segment tree stores intervals, and optimized for "which of these intervals contains a given point" queries.
# Interval tree stores intervals as well, but optimized for "which of these intervals overlap with a given interval" queries. It can also be used for point queries - similar to segment tree.
# Range tree stores points, and optimized for "which points fall within a given interval" queries.
# Binary indexed tree stores items-count per index, and optimized for "how
# many items are there between index m and n" queries.
