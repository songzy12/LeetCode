class Solution:
    def letterCasePermutation(self, S):
        """
        :type S: str
        :rtype: List[str]
        """
        if not S:
            return [S]
        import string
        # string.digits
        if S[0] in string.digits:
            return [S[0] + x for x in self.letterCasePermutation(S[1:])]
        # NOTE: lower(), upper()
        return [S[0].lower() + x for x in self.letterCasePermutation(S[1:])] + \
               [S[0].upper() + x for x in self.letterCasePermutation(S[1:])]
        
S = ''
print(Solution().letterCasePermutation(S))
        
