# Definition for a point
class Point:
    def __init__(self, a=0, b=0):
        self.x = a
        self.y = b

class Solution:
    # @param points, a list of Points
    # @return an integer
    def maxPoints(self, points):
        if len(points)==0 or len(points)==1 or len(points)==2:
            return len(points)
        d={}
        t = points[0]
        # strat from 2
        start = 2
        for i in points[1:]:
            # may be the same point
            if t.x == i.x and t.y == i.y:
                start += 1
                # care for the variable name
                for j in d:
                    d[j] += 1
            elif t.x == i.x:
                if (1,0,-i.x) in d.keys():
                    d[1, 0, -i.x] += 1
                else:
                    d[1, 0, -i.x] = start 
            else:
                # can not use divid(y = kx + b)
                A = i.y - t.y
                B = i.x - t.x
                C = i.y * B - A * i.x
                if A < 0 or A == 0 and B < 0:
                    A, B, C = -A, -B, -C
                g = self.gcd(self.gcd(A, abs(B)), abs(C))
                # make uniform
                A, B, C = A//g, B//g, C//g
                if (A, B, C) in d.keys():
                    d[A, B, C] += 1
                else:
                    d[A, B, C] = start
        # print(d)
        max1 = max([d[i] for i in d]) if len(d)!=0 else start - 1
        max2 = self.maxPoints(points[1:])
        return max(max1, max2)
    def gcd(self, a, b):
        if a < b:
            a, b = b, a
        if b == 0:
            return a
        return self.gcd(b, a % b)

for l in ([(0,0), (-1,-1), (2,2)],
          [(0,0), (1,1), (0,0)],
          [(1,1), (1,1), (1,1)],
          [(3,1),(12,3),(3,1),(-6,-1)],
          [(2,3), (3,3), (-5,3)]):
    print(Solution().maxPoints([Point(i[0], i[1]) for i in l]))
