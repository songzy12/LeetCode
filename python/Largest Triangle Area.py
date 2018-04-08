class Solution:
    def largestTriangleArea(self, points):
        """
        :type points: List[List[int]]
        :rtype: float
        """
        import math
        
        def get_area(p0, p1, p2):
            def get_length(p0, p1):
                return math.sqrt((p0[0]-p1[0])**2 + (p0[1]-p1[1])**2)
            a, b, c = get_length(p0,p1), get_length(p1,p2), get_length(p2,p0)
            def get_area_(a,b,c):
                p = (a+b+c)/2
                temp = p*(p-a)*(p-b)*(p-c)
                if abs(temp) < 1e-6: # NOTE: or there will be negative number
                    return 0
                return math.sqrt(temp)
            return get_area_(a, b, c)

        ans = 0
        length = len(points)
        for i in range(length):
            for j in range(i, length):
                for k in range(j, length):
                    temp_area = get_area(points[i], points[j], points[k])
                    if temp_area > ans:
                        ans = temp_area
        return ans

points = [[-35,19],[40,19],[27,-20],[35,-3],[44,20],[22,-21],[35,33],[-19,42],[11,47],[11,37]]
print(Solution().largestTriangleArea(points))
