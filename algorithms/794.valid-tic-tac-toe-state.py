class Solution:
    def validTicTacToe(self, board):
        """
        :type board: List[str]
        :rtype: bool
        """
        cnt_X = sum([row.count('X') for row in board])
        cnt_O = sum([row.count('O') for row in board])
        if cnt_X - cnt_O not in [0, 1]:
            return False

        def check_player(X):
            
            def check_row():
                cnt = 0
                for i in range(3):
                    if board[i][0] == board[i][1] == board[i][2] == X:
                        cnt += 1
                return cnt

            def check_column():
                cnt = 0
                for i in range(3):
                    if board[0][i] == board[1][i] == board[2][i] == X:
                        cnt += 1
                return cnt

            def check_diagonal():
                cnt = 0        
                if board[0][0] == board[1][1] == board[2][2] == X:
                    cnt += 1
                if board[0][2] == board[1][1] == board[2][0] == X:
                    cnt += 1
                return cnt

            
            return check_row() + check_column() + check_diagonal()

        check_X = check_player('X')
        check_O = check_player('O')
        if check_X > 1 or check_O > 1:
            return False
        if check_X == 1 and cnt_X - cnt_O == 0:
            return False
        if check_O == 1 and cnt_X - cnt_O == 1:
            return False
        return True

board = ["XOX", "O O", "XOX"]
board = ["XXX", "   ", "OOO"]
board = ["XOX", " X ", "   "]
board = ["O  ", "   ", "   "]
board = ["   ", "   ", "   "]
board = ["XXX","XOO","OO "]
board = ["OXX","XOX","OXO"]
print(Solution().validTicTacToe(board))
        
