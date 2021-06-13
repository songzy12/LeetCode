from functools import reduce
class Solution:
    # @param grid, a list of lists of integers
    # @return an integer

    def minPathSum(self, grid):
        if len(grid)==0 or len(grid[0])==0:
            return None
        m=len(grid)
        n=len(grid[0])
        for i in range(m-2,-1,-1):
            grid[i][n-1]+=grid[i+1][n-1]
        for j in range(n-2,-1,-1):
            grid[m-1][j]+=grid[m-1][j+1]
        for j in range(n-2,-1,-1):
            for i in range(m-2,-1,-1):
                grid[i][j]+=min(grid[i+1][j],grid[i][j+1])
        return grid[0][0]

##    # TLE
##    def minPathSum(self, grid):
##        return self.auxMinPathSum(grid, 0, 0)
##    def auxMinPathSum(self, grid, i, j):
##        if len(grid)==0 or len(grid[0])==0:
##            return 0
##        if i==len(grid)-1:
##            return reduce(lambda x,y:x+y, [grid[i][j0] for j0 in range(j,len(grid[0]))])
##        if j==len(grid[0])-1:
##            return reduce(lambda x,y:x+y, [grid[i0][j] for i0 in range(i,len(grid))])
##        else:                                                   
##            return grid[i][j]+min(self.auxMinPathSum(grid,i+1,j),\
##                   self.auxMinPathSum(grid,i,j+1))

grid=[[1,3]]
print(Solution().minPathSum(grid))
