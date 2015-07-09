class Solution:
    # @param {string} s
    # @return {integer}
    def lengthOfLongestSubstring(self, s):
        index = {}
        offset = result = current = 0
        for i in range(len(s)):
            if s[i] in index:
                result = max(result, current)
                offset = max(offset, index[s[i]])
                current = i - offset - 1
            index[s[i]] = i
            current += 1
        return max(result,current)

print(Solution().lengthOfLongestSubstring('a'))
print(Solution().lengthOfLongestSubstring('abba'))
print(Solution().lengthOfLongestSubstring('abcabc'))
