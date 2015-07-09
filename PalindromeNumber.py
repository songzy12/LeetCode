class Solution:
    # @param {integer} x
    # @return {boolean}
    def isPalindrome(self, x):
        if x < 0:
            return False
        temp = x # -2147483648
        y = 0
        while temp:
            y = (y * 10) + (temp % 10)
            temp //= 10 # // and /
        return y == x # reverse might overflow, can do half

print(Solution().isPalindrome(-1))
