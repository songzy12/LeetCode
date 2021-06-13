class Solution:
    # @param {character[][]} board
    # @return {boolean}
    def isValidSudoku(self, board):
        for row in range(9):
            m = {}
            for col in range(9):
                temp = board[row][col]
                if temp == '.':
                    continue
                if temp not in m:
                    m[temp] = 0
                else:
                    return False
        for col in range(9):
            m = {}
            for row in range(9):
                temp = board[row][col]
                if temp == '.':
                    continue
                if temp not in m:
                    m[temp] = 0
                else:
                    return False
        for col in [0, 3, 6]:
            for row in [0, 3, 6]:
                m = {}
                for i in range(3):
                    for j in range(3):
                        temp = board[row + i][col + j]
                        if temp == '.':
                            continue
                        if temp not in m:
                            m[temp] = 0
                        else:
                            return False
        return True

board = ['53..7....','6..195...','.98....6.',
         '8...6...3','4..8.3..1','7...2...6',
         '.6....28.','...419..5','....8..79']
print(Solution().isValidSudoku(board))
