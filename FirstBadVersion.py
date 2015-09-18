bad = [False, False, True]
def isBadVersion(version):
    return bad[version]

class Solution(object):
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        l, r = 1, n
        while l < r:
            m = l + (r-l) // 2
            if isBadVersion(m):
                r = m
            else:
                l = m+1
        return l

print Solution().firstBadVersion(2)
