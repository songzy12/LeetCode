class Solution:

    def reachingPoints(self, sx, sy, tx, ty):
        """
        :type sx: int
        :type sy: int
        :type tx: int
        :type ty: int
        :rtype: bool
        """
        while tx > sx and ty > sy:
            tx, ty = tx % ty, ty % tx
        return tx == sx and (sy - ty) % sx == 0 or \
            ty == sy and (sx - tx) % sy == 0


sx = 1
sy = 6
tx = 11
ty = 10

print(Solution().reachingPoints(sx, sy, tx, ty))

# 同样的思想，如果正着做过去很难的话不妨反过来想一想
