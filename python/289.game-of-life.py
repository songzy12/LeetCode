class Solution(object):
    def gameOfLife(self, board):
        """
        :type board: List[List[int]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        if not board:
            return
        m, n = len(board), len(board[0])
        for i in range(m):
            for j in range(n):
                count = 0
                for k in range(max(i-1, 0), min(i+2, m)):
                    for l in range(max(j-1, 0), min(j+2, n)):
                        if board[k][l] & 1:
                            count += 1
                if count == 3 or count - board[i][j] == 3:
                    board[i][j] |= 2 # else board[k][l] |= 0
        for i in range(m):
            for j in range(n):
                board[i][j] >>= 1

board = [[0, 1]]
for row in board:
    print row
print 
Solution().gameOfLife(board)
for row in board:
    print row
