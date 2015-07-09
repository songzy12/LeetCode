class Solution:
    # @param board, a 2D array
    # Capture all regions by modifying the input board in-place.
    # Do not return any value.
    def solve(self, board):
        # set boundary to 'A', then go through
        if len(board) == 0:
            return
        row = len(board)
        col = len(board[0])
        l = []
        for i in range(row):
            for j in range(col):
                if i == 0 or i == row-1 or j == 0 or j == col-1:
                    if board[i][j] == 'O':
                        board[i][j] = 'A'
                        l.append(i*col + j)
                        while len(l) != 0:
                            t = l.pop()
                            i1 = t // col
                            j1 = t % col
                            if i1 - 1 >= 0 and board[i1-1][j1]=='O':
                                board[i1-1][j1] = 'A'
                                l.append((i1-1)*col+j1)
                            if i1 + 1 < row and board[i1+1][j1]=='O':
                                board[i1+1][j1] = 'A'
                                l.append((i1+1)*col+j1)
                            if j1 - 1 >= 0 and board[i1][j1-1]=='O':
                                board[i1][j1-1] = 'A'
                                l.append(i1*col+j1-1)
                            if j1 + 1 < col and board[i1][j1+1]=='O':
                                board[i1][j1+1] = 'A'
                                l.append(i1*col+j1+1)
        for i in range(row):
            for j in range(col):
                if board[i][j] == 'O':
                    board[i][j] = 'X'
                if board[i][j] == 'A':
                    board[i][j] = 'O'

board = [list('XXXX'),list('XOOX'),list('XXOX'),list('XOXX')]
##board = [list("XXX"),list("XOX"),list("XXX")]
##board = [list("XXXXX"),
##         list("XOOOX"),
##         list("XXOOX"),
##         list("XXXOX"),
##         list("XOXXX")]

Solution().solve(board)
print(board)
