class Solution(object):
    def cutOffTree(self, forest):
        """
        :type forest: List[List[int]]
        :rtype: int
        """
        if not forest or not forest[0]:
            return 0
        
        hs = []
        for row in forest:
            hs.extend(filter(lambda x: x > 1, row))
        hs.sort()

        cur = [0, 0]
        cnt = 0
        
        def walk(cur, h):
            q = [cur + [0]]
            visited = {}
            visited[tuple(cur)] = True
            while q:
                x, y, step = q.pop(0)
                if forest[x][y] == h:
                    forest[x][y] = 1
                    return [x, y], step
                dx = [0,0,-1,1]
                dy = [-1,1,0,0]
                for i in range(4):
                    _x = x + dx[i]
                    _y = y + dy[i]
                    if _x < 0 or _x >= len(forest) or _y < 0 or _y >= len(forest[0]):
                        continue
                    if forest[_x][_y] == 0:
                        continue
                    if (_x, _y) not in visited:
                        visited[_x, _y] = True
                        q.append([_x, _y, step+1])
            return [-1, -1], -1

        # you can walk through trees
        while len(hs):
            h = hs.pop(0)
            
            cur, step = walk(cur, h)
            # print cur, step
            
            if step == -1:
                return -1
            cnt += step
        return cnt

# TLE
# this is not the algorithm's fault
# this is python's fault

forest = [[2,3,4],
          [0,0,5],
          [8,7,6]]
print Solution().cutOffTree(forest)
        
        
