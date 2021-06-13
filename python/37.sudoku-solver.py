class Solution:
    # @param board, a 9x9 2D array
    # Solve the Sudoku by modifying the input board in-place.
    # Do not return any value.
    def solveSudoku(self, board):
        # use an aux method recording the process by index
        self.auxSolveSudoku(board, 0)
    def auxSolveSudoku(self, board, index):
        if index==81:
            return True
        i=index//9
        j=index%9
        if board[i][j]!='.':
            return self.auxSolveSudoku(board,index+1)
        for k in self.valid(i,j,board):
            # just try every feasible choice, withdraw if improper
            board[i]=board[i][:j]+k+board[i][j+1:]
            if self.auxSolveSudoku(board, index+1):
                return True
            board[i]=board[i][:j]+'.'+board[i][j+1:]
        return False
    def valid(self, i,j,board):
        row=[x for x in board[i] if x!='.']
        column=[board[i1][j] for i1 in range(9) if board[i1][j]!='.']
        grid=[]
        for i1 in range(i-i%3, i+3-i%3):
            for j1 in range(j-j%3, j-j%3+3):
                if board[i1][j1]!='.':
                    grid.append(board[i1][j1])
        return list(filter(lambda x: x not in row and x not in column and x not in grid,\
                      [str(x) for x in range(1,10)]))
       
board=["..9748...","7........",".2.1.9...","..7...24.",".64.1.59.",".98...3..","...8.3.2.","........6","...2759.."]
Solution().solveSudoku(board)
for i in board:
    print(i)
