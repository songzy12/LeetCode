class Solution:
    # @param {string[]} strs
    # @return {string}
    def longestCommonPrefix(self, strs):
        if not strs:
            return ""
        for i, letter_group in enumerate(zip(*strs)): # use of zip
            if len(set(letter_group)) > 1:
                return strs[0][:i]
        else:
            return min(strs)
        
##        if not strs or not strs[0]:
##            return ''
##        i = 0
##        while i < len(strs[0]):
##            fine = True
##            t = strs[0][i]
##            for s in strs:
##                if i >= len(s) or s[i] != t:
##                    fine = False
##                    break
##            if not fine:
##                break
##            i += 1
##        return strs[0][:i]

print(Solution().longestCommonPrefix(['a', 'b']))
