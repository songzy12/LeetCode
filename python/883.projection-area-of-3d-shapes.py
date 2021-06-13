class Solution:
    def projectionArea(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        return sum([sum([1 for x in row if x]) for row in grid]) + \
               sum(max(row) for row in grid) + \
               sum(max(column) for column in zip(*grid))

grid = []
print(Solution().projectionArea(grid))