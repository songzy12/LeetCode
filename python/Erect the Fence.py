# Definition for a point.
class Point(object):
    def __init__(self, a=0, b=0):
        self.x = a
        self.y = b

class Solution(object):
    def outerTrees(self, points):
        """
        :type points: List[Point]
        :rtype: List[Point]
        """
        if not points:
            return points
        
        def get_ltl():
            ltl = points[0]
            for p in points:
                if p.x < ltl.x:
                    ltl = p
                if p.x == ltl.x and p.y < ltl.y:
                    ltl = p
            return ltl

        ltl = get_ltl()
        res = {ltl:1}

        def get_s(p):
            
            def to_left(a, b, c):
                # return a->b is left to a->c
                temp = (c.x-a.x)*(b.y-a.y) - (b.x-a.x)*(c.y-a.y)
                if temp != 0:
                    return temp > 0
                # if temp == 0, then True only when b lie in a->c
                return (b.x - a.x) * (c.x - a.x) > 0 and \
                       abs(b.x - a.x) > abs(c.x - a.x) or \
                       (b.y - a.y) * (c.y - a.y) > 0 and \
                       abs(b.y - a.y) > abs(c.y - a.y)
            def init_s(p):
                for t in points:
                    if t in res:
                        continue
                    return t
                return None
            s = init_s(p)
            if not s:
                return s
            for t in points:
                if t in [p, s]:
                    continue
                if to_left(p, s, t):
                    s = t
            return s
        
        s = get_s(ltl)
        while s and s != ltl:
            res[s] = 1
            s = get_s(s)
        return res.keys()

points = [[0,0],[0,1],[0,2],[1,2],[2,2],[3,2],[3,1],[3,0],[2,0]]
points = map(lambda p: Point(p[0], p[1]), points)
res = Solution().outerTrees(points)
for p in res:
    print 'p:', p.x, p.y

# [[0,0],[2,0],[3,0],[3,1],[3,2],[2,2],[1,2],[0,2],[0,1]]
# note the init_s and to_left 
