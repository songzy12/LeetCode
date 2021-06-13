class Solution:
    # @param {integer} n
    # @return {boolean}
    def isPowerOfTwo(self, n):
        if not n: # care for the boundary case
            return False
        while n % 2 == 0:
            n /= 2
        return True if n == 1 else False

n = input()
s = Solution()
while n != '.':
    print(s.isPowerOfTwo(int(n)))
    n = input()
