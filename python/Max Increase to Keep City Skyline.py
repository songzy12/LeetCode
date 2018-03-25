class Solution:
    def maxIncreaseKeepingSkyline(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        rows_max = list(map(max, grid))
        from functools import reduce
        grid_t = [[row[i] for row in grid] for i in range(len(grid[0]))]
        cols_max = list(map(max, grid_t))
        #print(list(cols_max))
        cnt = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                
                cnt += min(rows_max[i], cols_max[j]) - grid[i][j]
        return cnt

grid = [[3,0,8,4],[2,4,5,7],[9,2,6,3],[0,3,1,0]]
print(Solution().maxIncreaseKeepingSkyline(grid))
