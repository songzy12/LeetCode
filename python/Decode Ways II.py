class Solution(object):

    def numDecodings(self, S):
        MOD = 10**9 + 7
        e0, e1, e2 = 1, 0, 0
        for c in S:
            if c == '*':
                f0 = 9*e0 + 9*e1 + 6*e2
                f1 = e0
                f2 = e0
            else:
                f0 = (c > '0') * e0 + e1 + (c <= '6') * e2
                f1 = (c == '1') * e0
                f2 = (c == '2') * e0
            e0, e1, e2 = f0 % MOD, f1, f2
        return e0

    # e0 = current number of ways we could decode, ending on any number;
    # e1 = current number of ways we could decode, ending on an open 1;
    # e2 = current number of ways we could decode, ending on an open 2;

    '''
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """

        p = int(1e9 + 7)
        s = list(s) # TLE
        def helper(t):
            # how to make this elegant?
            if len(t) == 1:
                if t == '*':
                    return 9
                elif t == '0':
                    return 0
                else:
                    return 1                
            elif len(t) == 2:
                if t == ['*', '*']:
                    return 15
                elif t[0] == '*':
                    if t[1] <= '6':
                        return 2
                    else:
                        return 1
                elif t[1] == '*':
                    if t[0] == '1':
                        return 9 # * as 1 to 9
                    elif t[0] == '2':
                        return 6
                    else:
                        return 0
                else:
                    if t[0] == '0' or t[0] > '2' or t[0] == '2' and t[1] > '6':
                        return 0
                    return 1
            else:
                return 0
        
        a, b = helper(s[-1]), 1 # TLE, reduce space complexity
        for i in range(len(s)-2, -1, -1):
            a, b = (helper(s[i]) * a + helper(s[i:i+2]) * b) % p, a
        return a
    '''
    
s = '*1'
print Solution().numDecodings(s)
