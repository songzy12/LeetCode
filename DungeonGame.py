class Solution:
    # @param {integer[][]} dungeon
    # @return {integer}
    def calculateMinimumHP(self, dungeon):
        m = len(dungeon)
        n = len(dungeon[0])
        dungeon[m - 1][n - 1] = max(1, -(dungeon[m - 1][n - 1]) + 1)
        for i in range(n-2, -1, -1):
            dungeon[m - 1][i] = max(dungeon[m - 1][i + 1] - dungeon[m - 1][i],1)
        for i in range(m-2, -1, -1):
            dungeon[i][n - 1] = max(dungeon[i + 1][n - 1] - dungeon[i][n - 1],1)
        for i in range(m-2, -1, -1):
            for j in range(n-2, -1, -1):
                dungeon[i][j] = max(min(dungeon[i + 1][j], dungeon[i][j + 1]) - dungeon[i][j],1)
        return dungeon[0][0]
        
dungeon = [[1,-3,3],[0,-2,0],[-3,-3,-3]]#[[0,0,0],[1,1,-1]]
print(Solution().calculateMinimumHP(dungeon))
'''
dp[i][j]: min from [0,0] to [i,j],
[[1,-3,3],
 [0,-2,0],
 [-3,-3,-3]]
consider position [1,2],
1->0->-2->0, min is -1
1->-3->3->0, min is -2
but later one has more left
1->-3->3->0->-3 need 3,
while 1->0->-2->0->-3 need 5
'''
