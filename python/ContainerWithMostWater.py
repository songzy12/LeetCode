class Solution:
    # @param {integer[]} height
    # @return {integer}
    def maxArea(self, height):
        l = 0
        r = len(height) - 1
        result = 0
        while l<r:
            temp = min(height[l], height[r])*(r-l)
            if temp>result:
                result = temp
            if height[l]>height[r]:
                r-=1
            else:
                l+=1
        return result

import random
height = [random.randint(1, 10) for i in range(5)]
print(height)
print(Solution().maxArea(height))
