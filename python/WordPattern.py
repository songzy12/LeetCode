class Solution(object):
    def wordPattern(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        str = str.split(' ')
        if len(pattern)!=len(str):
            return False
        map_for_pattern = {}
        map_for_str = {}
        for i in range(len(pattern)):
            if pattern[i] not in map_for_pattern:
                if str[i] in map_for_str:
                    return False
                map_for_pattern[pattern[i]] = str[i]
                map_for_str[str[i]] = True
            else:
                if map_for_pattern[pattern[i]] != str[i]:
                    return False
        return True

pattern = 'abba'
str = 'dog cat cat dog'
print Solution().wordPattern(pattern, str)
