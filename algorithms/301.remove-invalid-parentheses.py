class Solution(object):
##    def removeInvalidParentheses(self, s):
##        """
##        :type s: str
##        :rtype: List[str]
##        """
##        def isValid(s):
##            res = 0
##            for c in s:
##                if c == '(':
##                    res += 1
##                elif c == ')':
##                    res -= 1
##                    if res < 0:
##                        return False
##            return res == 0
##                    
##        level = [s]
##        while level:
##            valid = filter(isValid, level)
##            if valid:
##                return valid
##            level = {s[:i]+s[i+1:] for s in level for i in range(len(s))} # set

    def removeInvalidParentheses(self, s):
        level = {s}
        while True:
            valid = []
            for s in level:
                try:
                    eval('0,' + filter('()'.count, s).replace(')', '),'))
                    # filter('()'.count, s) only leaves ['(',')'] in s
                    valid.append(s)
                except:
                    pass
            if valid:
                return valid
            level = {s[:i] + s[i+1:] for s in level for i in range(len(s))}

s = "()())()" # ["()()()", "(())()"]
s = ""
print Solution().removeInvalidParentheses(s)
