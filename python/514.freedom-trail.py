class Solution(object):
    def findRotateSteps(self, ring, key):
        """
        :type ring: str
        :type key: str
        :rtype: int
        """
        m = {}
        def get_ro_rc(char, co):
            if ring[co] == char:
                return co, 0
            if ring[co+1:].find(char) != -1:
                return ring[co+1:].find(char) + 1 + co, ring[co+1:].find(char) + 1
            if ring[:co].find(char) != -1:
                return ring[:co].find(char), ring[:co].find(char) +  len(ring) - co
            return -1
        def get_lo_lc(char, co):
            if ring[co] == char:
                return co, 0
            if ring[:co].rfind(char) != -1:
                return ring[:co].rfind(char), co - ring[:co].rfind(char)
            if ring[co+1:].rfind(char) != -1:
                return ring[co+1:].rfind(char) + 1 + co, len(ring) - 1 - ring[co+1:].rfind(char)
            return -1             
        def dp(offset, key):
            if (offset, key) in m:
                return m[(offset, key)]
            if not key:
                return 0
            ro, rc = get_ro_rc(key[0], offset)
            lo, lc = get_lo_lc(key[0], offset)
            #print ring, offset, ring[offset], key[0]
            #print lo, lc, ro, rc
            m[(offset, key)] = min(dp(lo, key[1:])+lc, dp(ro, key[1:])+rc)
            return m[(offset, key)]
        
        return dp(0, key) + len(key)

if __name__ == '__main__':
    ring = "godding"
    key = "godding" 
    print Solution().findRotateSteps(ring, key)
    
# There might be some duplicate characters in both strings
# so greedy will not work

# then just use dp?
# dp(ring, offset, key) = min(dp(ring, left_offset, key[1:]), dp(ring, right_offset, key[1:]))
# the number of state is just len(ring) * len(key)
