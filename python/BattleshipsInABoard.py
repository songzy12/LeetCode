# one pass, O(1) extra memory, without modifying

class Solution(object):
    def countBattleships(self, board):
        """
        :type board: List[List[str]]
        :rtype: int
        """
        count = 0
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] != 'X':
                    continue
                if i > 0 and board[i-1][j] == 'X' or\
                   j > 0 and board[i][j-1] == 'X':
                    continue
                count += 1
        return count

board = ['xx']
print Solution().countBattleships(board)

# count only those that are the "first" cell of the battleship
