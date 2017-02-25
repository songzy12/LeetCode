# You are given several projects. 
# For each project i, it has a pure profit Pi and a minimum capital of Ci is needed to start the corresponding project. 
# Initially, you have W capital.
# When you finish a project, you will obtain its pure profit and the profit will be added to your total capital.

class Solution(object):
    def findMaximizedCapital(self, k, W, Profits, Capital):
        import heapq
        current = []
        future = sorted(zip(Capital, Profits))[::-1]
        for _ in range(k):
            while future and future[-1][0] <= W:
                heapq.heappush(current, -future.pop()[1])
            if current:
                W -= heapq.heappop(current)
        return W
    
    #===========================================================================
    # def __init__(self):
    #     self.dp = {}
    #      
    # def helper(self, k, W, index):
    #     # what is the maximum gain?
    #     if k == 0:
    #         return 0
    #     if index == len(self.Profits):
    #         return 0
    #     if (k, W, index) in self.dp:
    #         return self.dp[(k, W, index)]
    #     if self.Capital[index] <= W:
    #         self.dp[(k, W, index)] = max(self.Profits[index]+self.helper(k-1, W+self.Profits[index], index+1),
    #                                      self.helper(k, W, index+1)) 
    #     else:
    #         self.dp[(k, W, index)] = self.helper(k, W, index+1) 
    #     return self.dp[(k, W, index)] 
    #          
    #   
    # def findMaximizedCapital(self, k, W, Profits, Capital):
    #     """
    #     :type k: int
    #     :type W: int
    #     :type Profits: List[int]
    #     :type Capital: List[int]
    #     :rtype: int
    #     """
    #     self.Profits = Profits
    #     self.Capital = Capital
    #     return W+self.helper(k, W, 0) 
    #===========================================================================

if __name__ == "__main__":        
    k=2
    W=0
    Profits=[1,2,3]
    Capital=[0,1,1]
    print Solution().findMaximizedCapital(k, W, Profits, Capital)
    
# Initial Public Offerings
# first thought: use dp

# TLE

# Greedy 
# The more capital W you have now, the more maximum capital you will eventually earn.
# Working on any doable project with positive P[i] > 0 increases your capital W.

# always work on the most profitable project P[i] first as long as it is doable 
# until we reach maximum k projects or all doable projects are done.