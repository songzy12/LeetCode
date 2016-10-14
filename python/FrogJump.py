# Given a list of stones' positions (in units) in sorted ascending order, 
# determine if the frog is able to cross the river by landing on the last stone. 
# Initially, the frog is on the first stone and assume the first jump must be 1 unit. 
# If the frog's last jump was k units, 
# then its next jump must be either k - 1, k, or k + 1 units.

class Solution(object):
    def canCross(self, stones):
        """
        :type stones: List[int]
        :rtype: bool
        """
        m = {}
        for stone in stones:
            m[stone] = set()
        m[stones[0]].add(1)
        for stone in stones:
            if not m[stone]:
                continue
            for step in m[stone]:
                if stone + step not in m:
                    continue
                if stone + step == stones[-1]:
                    return True
                if step - 1:
                    m[stone + step].add(step - 1)
                m[stone + step].add(step)
                m[stone + step].add(step + 1)
        return False
        
stones =  [0,1,2,3,4,8,9,11]
print Solution().canCross(stones)

# 3**n, if record all possible destination after n jumps
# backward, then n**3

# from left to right
# use map to represent a mapping from the stone (not index) to the steps that can be taken from this stone.
# TLE, change list to set