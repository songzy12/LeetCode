class Solution:
    def asteroidCollision(self, asteroids):
        """
        :type asteroids: List[int]
        :rtype: List[int]
        """
        stack = []
        for a in asteroids:
            if not stack:
                stack.append(a)
                continue
            if stack[-1] < 0:
                stack.append(a)
                continue
            if a > 0:
                stack.append(a)
                continue
            while stack and stack[-1] > 0 and abs(a) > stack[-1]:
                stack.pop(-1)
            if not stack or stack[-1] < 0:
                stack.append(a)
                continue
            
            if abs(a) < stack[-1]:
                continue
            if abs(a) == stack[-1]:
                stack.pop(-1)
                continue
            
        return stack

asteroids = [5, 10, -5]
print(Solution().asteroidCollision(asteroids))
                
