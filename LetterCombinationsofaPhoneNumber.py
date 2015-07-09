class Solution:
    # @param {string} digits
    # @return {string[]}
    def __init__(self):
        self.m = {'2':'abc', '3':'def', '4':'ghi', '5':'jkl', '6':'mno', '7':'pqrs', '8':'tuv', '9':'wxyz'}
    def letterCombinations(self, digits):
        return [] if not digits else self.aux(digits, 0)
    def aux(self, digits, i):
        return [''] if i == len(digits) else [s + t for t in self.aux(digits, i+1) for s in self.m[digits[i]]]
        
##    def letterCombinations(self, digits):
##        if '' == digits: return []
##        kvmaps = {
##            '2': 'abc',
##            '3': 'def',
##            '4': 'ghi',
##            '5': 'jkl',
##            '6': 'mno',
##            '7': 'pqrs',
##            '8': 'tuv',
##            '9': 'wxyz'
##        }
##        return reduce(lambda acc, digit: [x + y for x in acc for y in kvmaps[digit]], digits, [''])

print(Solution().letterCombinations('234'))

    
