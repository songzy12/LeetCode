class Solution(object):

    def updateBoard(self, board, click):

        """
        :type board: List[List[str]]
        :type click: List[int]
        :rtype: List[List[str]]
        """
        x, y = click
        if board[x][y] == 'M':
            board[x][y] = 'X'
            return board
        def count_mine(x, y):
            ans = 0
            for dx in range(-1, 2):
                for dy in range(-1, 2):
                    if not dx and not dy:
                        continue
                    x0 = x + dx
                    y0 = y + dy
                    if 0 <= x0 < len(board) and 0 <= y0 < len(board[0]) and board[x0][y0] == 'M':
                        ans += 1
            return ans
        count = count_mine(x,y)
        if count != 0:
            board[x][y] = str(count)
            return board
        board[x][y] = 'B'
        
        for dx in range(-1, 2):
            for dy in range(-1, 2):
                if not dx and not dy:
                    continue
                x0 = x + dx
                y0 = y + dy
                if 0 <= x0 < len(board) and 0 <= y0 < len(board[0]) and board[x0][y0] == 'E':
                    self.updateBoard(board, [x0, y0]) 
        return board
