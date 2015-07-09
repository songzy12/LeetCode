class Solution:
    # @param digits, a list of integer digits
    # @return a list of integer digits
    def plusOne(self, digits):
        return [int(x) for x in str(int("".join([str(n) for n in digits]))+1)]

digits=[1,2,3]
print(Solution().plusOne(digits))
