class Solution(object):
    def candyCrush(self, board):
        """
        :type board: List[List[int]]
        :rtype: List[List[int]]
        """

        def check_row(row):
            j = 0
            out = []
            while j + 2 < len(row):
                if row[j] and row[j] == row[j+1] == row[j+2]:
                    while j + 2 < len(row) and row[j] and row[j] == row[j+1] == row[j+2]:
                        out.append(j)
                        j += 1
                    out.append(j)
                    out.append(j+1)
                    j += 1
                j += 1
            return out

        def check_rows():
            ans = []
            for i in range(len(board)):
                temp = check_row(board[i])
                ans += [(i, j) for j in temp]

            for j in range(len(board[0])):
                temp = check_row([x[j] for x in board])
                ans += [(i, j) for i in temp]
            return ans

        def clear(ans):
            for i, j in ans:
                board[i][j] = 0

            for j in range(len(board[0])):
                temp = []
                for i in range(len(board)-1, -1, -1):
                    if board[i][j]:
                        temp.append(board[i][j])

                l = 0
                for i in range(len(board)-1, -1, -1):
                    if l < len(temp):
                        board[i][j] = temp[l]
                        l += 1                        
                    else:
                        board[i][j] = 0
                
        ans = check_rows()
        while ans:
            clear(ans)
            
            ans = check_rows()
        return board

board = [[110,5,112,113,114],
         [210,211,5,213,214],
         [310,311,3,313,314],
         [410,411,412,5,414],
         [5,1,512,3,3],
         [610,4,1,613,614],
         [710,1,2,713,714],
         [810,1,2,1,1],
         [1,1,2,2,2],
         [4,1,4,4,1014]]

board =  Solution().candyCrush(board)
for row in board:
    print row
            
