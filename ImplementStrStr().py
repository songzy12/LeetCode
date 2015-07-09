class Solution:
    # @param haystack, a string
    # @param needle, a string
    # @return a string or None
    def strStr(self, haystack, needle):
        return None if haystack.find(needle)==-1 else \
               haystack[haystack.find(needle):]

haystack="Now I bet you are just fine"
needle="you"
print(Solution().strStr(haystack, needle))
