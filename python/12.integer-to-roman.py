class Solution:
    # @param {integer} num
    # @return {string}
    def intToRoman(self, num):
        roman  = {1000: 'M', 900: 'CM', 500: 'D', 400: 'CD', 100: 'C', 90: 'XC', 50: 'L', 40: 'XL', 10: 'X', 9: 'IX', 5: 'V', 4: 'IV', 1: 'I'}
        s = ""
        for i in sorted(roman.keys(), reverse = True):
            while num >= i:
                s += roman[i]
                num -= i
        return s

##        thousands = num//1000
##        hundreds = num%1000//100
##        tens = num%100//10
##        ones = num%10
##        res = ''
##        res += 'M'*thousands
##        res += 'CM' if hundreds == 9 else \
##               'D'+'C'*(hundreds-5) if 5<= hundreds<9 else\
##               'CD' if hundreds == 4 else\
##               'C'*hundreds
##        res += 'XC' if tens == 9 else\
##               'L'+'X'*(tens-5) if 5<=tens<9 else\
##               'XL' if tens == 4 else\
##               'X'*tens
##        res += 'IX' if ones == 9 else\
##               'V'+'I'*(ones-5) if 5<=ones<9 else\
##               'IV' if ones == 4 else\
##               'I'*ones
##        return res

print Solution().intToRoman(1066)
