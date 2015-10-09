class Solution(object):
    def largestRectangleArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        if not height:
            return 0
        q = [-1]
        ans = 0
        for i in range(len(height)):
            while q[-1] != -1 and height[i] < height[q[-1]]:
                # right i, left q[-2], height[q[-1]]
                temp = height[q[-1]]*(i-q[-2]-1) 
                ans = max(temp, ans)
                q.pop()
            q += i,
        # i = len(height)
        while q[-1] != -1:
            temp = height[q[-1]]*(len(height)-q[-2]-1) 
            ans = max(temp, ans)
            q.pop()
        return ans

height = [2,1,2]
print Solution().largestRectangleArea(height)
