class Solution(object):
    def __init__(self):
        self.ans = 0
        
    def dfs(self, avaliable, cur, n):
        if cur == n+1:
            self.ans += 1
            return
        for i, t in enumerate(avaliable):
            if i == 0:
                continue
            if not t:
                continue
            if cur % i == 0 or i % cur == 0:
                avaliable[i] = False
                self.dfs(avaliable, cur + 1, n)
                avaliable[i] = True
    
    def countArrangement(self, N):
        """
        :type N: int
        :rtype: int
        """
        avaliable = [True]*(N+1)
        self.dfs(avaliable, 1, N)
        return self.ans
        
        
# numbers can be placed at position i is i's divider or multiplier
# number n can be placed at position that is n's divider or multiplier

# use dfs
