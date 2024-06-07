class Solution:
    # @return an integer
    def divide(self, dividend, divisor):

        a=abs(dividend)
        b=abs(divisor)
        ans=i=0

        # compute 2**(i-1) * b < a <= 2**i * b
        while a>b:
            i+=1
            b=b<<1
        
        while i>=0:
            # then we substract b from a one by one
            # record which step we are, and change the ans
            if a>=b:
                a-=b
                ans+=1<<i
            b=b>>1
            i-=1
        return ans if (dividend>>31)==(divisor>>31) else -ans
    
##        out=0
##        sign=1 if ((dividend>0 and divisor>0) or (dividend<0 and divisor<0)) else -1
##        dividend=abs(dividend)
##        divisor=abs(divisor)
##        while dividend>=divisor:
##            dividend-=divisor
##            out+=1
##        return out if sign==1 else -out

print(Solution().divide(-1,1))
