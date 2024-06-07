class Solution:
    # @param {string} s1
    # @param {string} s2
    # @return {boolean}
    def isScramble(self, s1, s2):
        # print s1, s2
        if s1 == s2:
            return True
        if sorted(s1) != sorted(s2):
            return False
        for pre in range(1, len(s1)):
            # not pre = len(s1)//2
            if self.isScramble(s1[:pre], s2[:pre]) and \
               self.isScramble(s1[pre:], s2[pre:]) or \
               self.isScramble(s1[:pre], s2[-pre:]) and \
               self.isScramble(s1[pre:], s2[:-pre]):
                return True
        return False

s1 = 'abb'
s2 = 'bab'
print(Solution().isScramble(s1, s2))
