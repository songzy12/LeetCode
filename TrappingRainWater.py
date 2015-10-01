class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        if not height:
            return 0
        l, r = 0, len(height)-1
        ans = lower = 0
        level = min(height[l], height[r])
        while l < r:
            # count from lower side
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
            lower = min(height[l], height[r])
            # level is the safe height
            if lower > level:
                level = lower
            ans += level - lower
        return ans

height = [0,1,0,2,1,0,1,3,2,1,2,1]
print Solution().trap(height)
