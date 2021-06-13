class Solution:
    # @param n, an integer
    # @return an integer
    def hammingWeight(self, n):
##        n=bin(n)
##        x=0
##        for c in n:
##            x=x+1 if c=='1' else x
##        return x

        return len([char for char in bin(n) if char == '1'])

##        return bin(n)[2:].count('1')

print(Solution().hammingWeight(11))

