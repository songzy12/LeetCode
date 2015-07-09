class Solution:
    # @param {string} s
    # @param {string} t
    # @return {boolean}
    def isIsomorphic(self, s, t):
        m = {}
        m2 = {} # since no two can map to one
        for i in range(len(s)):
            if s[i] not in m:
                if t[i] in m2:
                    return False
                m[s[i]] = t[i]
                m2[t[i]] = 1
            else:
                if m[s[i]]!=t[i]:
                    return False
        return True

s, t = 'paper', 'title'
s, t = 'ab', 'aa'
print(Solution().isIsomorphic(s, t))
                
            
        
