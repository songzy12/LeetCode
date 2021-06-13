class Solution(object):
    def findMinStep(self, board, hand):
        """
        :type board: str
        :type hand: str
        :rtype: int
        """
        def clear(board):
            flag = 1 # since there may be multiple clear round
            while flag:
                i = j = 0
                flag = 0
                while i < len(board):
                    while j < len(board) and board[j] == board[i]:
                        j += 1
                    if j - i >= 3:
                        board = board[:i] + board[j:]
                        flag = 1
                    i = j
            return board
            
        def helper(board, hand):
            #print board,
            board = clear(board)
            #print board
            if not board:
                return 0
            if not sum(hand.values()):
                return 6
            res = 6
            i = 0
            while i < len(board):
                missing = 2
                if i < len(board) - 1 and board[i+1] == board[i]:
                    missing = 1
                    i += 1
                if hand[board[i]] >= missing:
                    hand[board[i]] -= missing
                    res = min(res, missing + helper(board[:i] + board[i]*missing + board[i:], hand))
                    hand[board[i]] += missing
                i += 1
            return res
            
        #print clear("RRRRBBWW")
        from collections import Counter
        hand = Counter(hand)
        res = helper(board, hand)
        return res if res < 6 else -1
        
if __name__ == '__main__':
    board, hand = "RBYYBBRRB", "YRBGB"
    print Solution().findMinStep(board, hand)
    
