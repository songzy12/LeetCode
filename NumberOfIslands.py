class Solution:
    # @param grid, a list of list of characters
    # @return an integer
    def numIslands(self, grid):
        if len(grid) == 0:
            return 0
        result = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    result += 1
                    # just use DFS
                    self.expand(i, j, grid)
        return result
    def expand(self, i, j, grid):
        if i < 0 or i >= len(grid):
            return
        if j < 0 or j >= len(grid[0]):
            return
        if grid[i][j] == '0':
            return
        grid[i] = grid[i][:j]+'0'+grid[i][j+1:]
        self.expand(i-1, j, grid)
        self.expand(i+1, j, grid)
        self.expand(i, j-1, grid)
        self.expand(i, j+1, grid)

for grid in [["10011101100000000000",
              "10011001000101010010",
              "00011110101100001010",
              "00011001000111001001",
              "00000001110000000000",
              "10000101011000000101",
              "00010001010101010101",
              "00010100110101101110",
              "00001001100001000101",
              "00100100000100100010",
              "10010000000100101010",
              "01000101011011101100",
              "11010000100000010001",
              "01001110001111101000",
              "00111000110001010000",
              "10010100001000101011",
              "10100000010001010000",
              "01100011101010111100",
              "01000011001010010011",
              "00000011110100011000"],
             ["111111111",
              "100000001",
              "101010101",
              "101111101",
              "101010101",
              "100000001",
              "111111111"],
             ['111',
              '101',
              '111'],
             ['11110',
              '11010',
              '11000',
              '00000'],
             ['11000',
              '11000',
              '00100',
              '00011']]:
# only this and last line are not enough
    print(Solution().numIslands(grid))
