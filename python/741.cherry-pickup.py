# https://leetcode.com/problems/cherry-pickup/description/
# https://leetcode.com/problemset/algorithms/?difficulty=Hard&status=Todo


class Solution:

    def cherryPickup(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """

# 走过去之后再回来，各条路径是互相影响的
# 并不能使用贪心算法

# wow 看一眼数据范围吧，1 <= N <= 50
# dp: 假设有两个人同时出发，写一个递归
