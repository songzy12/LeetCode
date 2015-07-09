class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
##        t=0
##        p=2**31
##        # there are 32 bits in total
##        for i in bin(n)[:1:-1]:
##            t=t+int(i)*p
##            p=p//2
##        return t

##        o = bin(n).lstrip('0b').zfill(32)
##        n = int(o[::-1],2)
##        return n
        r=0
        for i in range(32):
            r = ((n>>i)&1) + r*2
        return r
    
n= 43261596
print(Solution().reverseBits(n))
