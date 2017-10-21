class Solution(object):
    def maxAreaOfIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        if not grid:
            return 0

        ans = 0
        visited = [[False for i in range(len(grid[0]))] for j in range(len(grid))]

        def valid(x, y):
            return 0 <= x < len(grid) and 0 <= y < len(grid[0]) and \
                   not visited[x][y] and grid[x][y]
        
        def bfs(i, j):
            q = [(i, j)]
            visited[i][j] = True
            res = 1
            dirs = [[0, -1], [0, 1], [-1, 0], [1, 0]]
            while q:
                x, y = q.pop(0)
                for dx, dy in dirs:
                    if valid(x + dx, y + dy):
                        
                        q.append([x + dx, y + dy])
                        visited[x+dx][y+dy] = True
                        res += 1
            return res                
            
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if visited[i][j] or not grid[i][j]:
                    continue
                cur = bfs(i, j)
                if cur > ans:
                    ans = cur
        return ans
        
grid = [ [0,0,1,0,0,0,0,1,0,0,0,0,0],
         [0,0,0,0,0,0,0,1,1,1,0,0,0],
         [0,1,1,0,1,0,0,0,0,0,0,0,0],
         [0,1,0,0,1,1,0,0,1,0,1,0,0],
         [0,1,0,0,1,1,0,0,1,1,1,0,0],
         [0,0,0,0,0,0,0,0,0,0,1,0,0],
         [0,0,0,0,0,0,0,1,1,1,0,0,0],
         [0,0,0,0,0,0,0,1,1,0,0,0,0]]

print Solution().maxAreaOfIsland(grid)
