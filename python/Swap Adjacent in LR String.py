# https://leetcode.com/problems/swap-adjacent-in-lr-string/description/

class Solution:
    def canTransform(self, start, end):
        """
        :type start: str
        :type end: str
        :rtype: bool
        """
        # here start and end are not symmetric
        for t in 'LRX':
            if start.count(t) != end.count(t):
                return False

##        def convert(s):
##            res = []
##            last = ''
##            cnt = 0
##            for t in s:
##                if t == 'X':
##                    continue
##                if not last:
##                    last = t
##                    cnt += 1
##                    res.append(t)
##                    continue
##                if t != last:
##                    res.append(cnt)
##                    cnt = 0
##                    last = t
##                else:
##                    cnt += 1
##            return tuple(res)
##        if convert(start) != convert(end):
##            return False

        if start.replace('X','') != end.replace('X', ''):
            return False
    
        def check(start, end, token):
            l1 = l2 = 0
            for i in range(len(start)):
                if start[i] == token:
                    l1 += 1
                if end[i] == token:
                    l2 += 1
                if l1 > l2:
                    return False
            return True
        return check(start, end, 'L') and check(start[::-1], end[::-1], 'R')
        

start = "XXRXXLXXXX"
end = "XXXXRXXLXX"

start = 'RL'
end = 'LR'
print(Solution().canTransform(start, end))
