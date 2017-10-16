class Solution(object):
    def fallingSquares(self, positions):
        """
        :type positions: List[List[int]]
        :rtype: List[int]
        """
        ans = []
        intervals = []

        def compute(l, r):
            cur_h = 0
            for l0, r0, h0 in intervals:
                if l0 < l < r0 or l0 < r < r0 or \
                   l0 <= l and r0 >= r or \
                   l <= l0 and r >= r0: # =
                    cur_h = max(cur_h, h0)            
            return cur_h

        cur_max = 0
        for l, h in positions:
            r = l + h 
            cur_h = compute(l, r)
            cur_max = max(cur_h + h, cur_max)
            ans.append(cur_max)
            intervals.append([l, r, cur_h + h])
        return ans

positions = [[1,2],[1,3]]
print Solution().fallingSquares(positions)

# no need to use interval tree or segment tree
# maybe I should learn them again

# also, notice that positions.length <= 1000
# so a n^2 solution is bearable

# ok, segment tree is also right
