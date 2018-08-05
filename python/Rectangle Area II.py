# https://leetcode.com/problems/rectangle-area-ii/description/


class Solution:

    def rectangleArea(self, rectangles):
        """
        :type rectangles: List[List[int]]
        :rtype: int
        """

rectangles = [[0, 0, 2, 2], [1, 0, 2, 3], [1, 0, 3, 1]]
print(Solution().rectangleArea(rectangles))

# 按 x 顺序保存所有的点
# 然后二分搜索并更新点集