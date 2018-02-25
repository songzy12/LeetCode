class Solution:
    def escapeGhosts(self, ghosts, target):
        """
        :type ghosts: List[List[int]]
        :type target: List[int]
        :rtype: bool
        """
        for ghost in ghosts:
            if abs(ghost[0] - target[0]) + abs(ghost[1] - target[1]) <= \
               abs(target[0]) + abs(target[1]):
                return False
        return True

ghosts = [[1,0], [0,3]]
target = [0,1]
print(Solution().escapeGhosts(ghosts, target))
