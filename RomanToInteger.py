class Solution:
    # @param {string} s
    # @return {integer}
    def romanToInt(self, s):
        val = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        ans = val[s[-1]]
        for i in range(len(s) - 1):
            if val[s[i]] < val[s[i + 1]]:
                ans -= val[s[i]]
            else:
                ans += val[s[i]]
        return ans
    
##        res = index = 0
##        length = len(s)
##        while index < length and s[index] == 'M':
##            res += 1000
##            index += 1
##        if index + 1 < length and s[index:index+2] in ('CM','CD'):
##            res += 900 if s[index+1] == 'M' else 400
##            index += 2
##        if index < length and s[index] == 'D':
##            res += 500
##            index += 1
##        while index < length and s[index] == 'C':
##            res += 100
##            index += 1
##        if index+1 < length and s[index:index+2] in ('XC','XL'):
##            res += 90 if s[index+1] == 'C' else 40
##            index += 2
##        if index < length and s[index] == 'L':
##            res += 50
##            index += 1
##        while index < length and s[index] == 'X':
##            res += 10
##            index += 1
##        if index+1 < length and s[index:index+2] in ('IX','IV'):
##            res += 9 if s[index+1] == 'X' else 4
##            index += 2 
##        if index < length and s[index] == 'V':
##            res += 5
##            index += 1
##        while index < length and s[index] == 'I':
##            res += 1
##            index += 1
##        return res
            
print Solution().romanToInt('MCMXCIX')            
        
        
