class Solution(object):
    def __init__(self):
        self.ans = []
        self.n = -1
    def DFS(self, queens, xy_dif, xy_sum):
        # if (x,y) in queens, then (p,q) with \
        # p+q == x+y or p-q == x-y not in queens
        p = len(queens) # now the p-th row
        if p == self.n:
            self.ans += queens,
            return
        for q in range(self.n):
            if q not in queens and p-q not in xy_dif and p+q not in xy_sum:
                self.DFS(queens+[q], xy_dif+[p-q], xy_sum+[p+q])
        
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        self.n = n
        self.DFS([],[],[])
        return [['.'*i+'Q'+'.'*(n-i-1) for i in sol] for sol in self.ans]

print Solution().solveNQueens(4)
