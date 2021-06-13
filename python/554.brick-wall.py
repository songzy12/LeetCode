class Solution(object):
    def leastBricks(self, wall):
        """
        :type wall: List[List[int]]
        :rtype: int
        """
        from collections import defaultdict
        m = defaultdict(int)
        for row in wall:
            prefix = 0
            for width in row:
                prefix += width
                m[prefix] += 1
            m[prefix] -= 1
        return len(wall) - max(m.values())

if __name__ == '__main__':
    wall = [[1,2,2,1],
            [3,1,2],
            [1,3,2],
            [2,4],
            [3,1,2],
            [1,3,1,1]]
    print Solution().leastBricks(wall)
