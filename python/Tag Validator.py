# https://leetcode.com/problems/tag-validator/description/


class Solution:

    def isValid(self, code):
        """
        :type code: str
        :rtype: bool
        """
        stack = []
        i = 0
        while i < len(code):
            if i > 0 and not stack:
                return False
            if code.startswith('<![CDATA[', i):
                j = i + len('<![CDATA[')
                i = code.find(']]>', j)
                if i < 0:
                    return False
                i += len(']]>')
            elif code.startswith('</', i):
                j = i + len('</')
                i = code.find('>', j)
                if i < 0 or i == j or i - j > 9:
                    return False
                for k in range(j, i):
                    if not code[k].isupper():
                        return False
                s = code[j:i]
                i += 1
                if not stack or stack[-1] != s:
                    return False
                stack.pop(-1)
            elif code.startswith('<', i):
                j = i + len('<')
                i = code.find('>', j)
                if i < 0 or i == j or i - j > 9:
                    return False
                for k in range(j, i):
                    if not code[k].isupper():
                        return False
                s = code[j:i]
                i += 1
                stack += s,
            else:
                i += 1
        return not stack


code = "<DIV>This is the first line <![CDATA[<div>]]></DIV>"
print(Solution().isValid(code))

# 还是要善用 startswith 以及 find
# find 和 index 的区别在于 index 会报错， find 会返回 -1
