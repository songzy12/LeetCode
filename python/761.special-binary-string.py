# https://leetcode.com/contest/weekly-contest-66/problems/special-binary-string/

class Solution:
    def makeLargestSpecial(self, S):
        """
        :type S: str
        :rtype: str
        """
        # greedy algorithm
        # but not complete, you need to do recusion inside the higher level special string

        def split(S):
            res = []
            temp = []
            cnt = 0
            for t in S:
                temp.append(t)
                if t == '1':
                    cnt += 1                    
                else:
                    cnt -= 1
                    if cnt == 0:
                        res.append(''.join(temp))
                        temp = []
            return res

        parts = split(S)
    
        if not parts:
            return ''
        if len(parts) == 1:
            return '1' + self.makeLargestSpecial(parts[0][1:-1]) + '0'

        def cmp(a, b):
            
            for x, y in zip(list(a), list(b)):
                if not x or not y:
                    return 0
                if x < y:
                    return 1
                if x > y:
                    return -1
            return 0

        import functools
        parts = list(map(self.makeLargestSpecial, parts))
        parts.sort(key=functools.cmp_to_key(cmp)) # NOTE: remember the cmp function
        return ''.join(parts)

S = "101110110011010000"
print(Solution().makeLargestSpecial(S))
        
        

