# https://leetcode.com/contest/weekly-contest-76/problems/bricks-falling-when-hit/


class Solution:

    def hitBricks(self, grid, hits):
        """
        :type grid: List[List[int]]
        :type hits: List[List[int]]
        :rtype: List[int]
        """
        
        

# 看起来每次都做一个 BFS 就可以了呀
# 只有一个 BFS 是不够的，可能会出现悬空的相邻两个
# 每次都要重新检查，不用在最开始记录状态了

# 啊就是把这个过程反过来！
# 最开始把所有都去掉，然后查看其它还连接着的
# 然后按照逆序一个一个接回来，看能影响到多少邻居