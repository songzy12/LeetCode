class Solution:
    # @param s, a string
    # @return a boolean
    def isNumber(self, s):
        try:
            float(s)
            return True
        except Exception as e1:
            return False

print(Solution().isNumber("+ 1"))
            
