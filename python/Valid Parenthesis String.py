class Solution(object):
    def checkValidString(self, s):
        """
        :type s: str
        :rtype: bool
        """
        pos = set({0}) # possible numbef of unmatched (
        for c in s:
            temp = set()
            if c == ')':
                for n in pos:
                    if n > 0:
                        temp.add(n - 1)
            elif c == '(':
                for n in pos:
                    temp.add(n + 1)
            else:
                for n in pos:
                    temp.add(n)
                    temp.add(n + 1)
                    if n > 0:
                        temp.add(n - 1)
            if not temp:
                return False
            pos = temp
        return 0 in pos

s = "(*()"
print Solution().checkValidString(s)
