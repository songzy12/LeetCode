class Solution:
    # @return an integer
    def reverse(self, x):

        lx=str(abs(x))
        lx=lx[::-1]
        return -int(lx) if x<0 else int(lx)
    
##        sign= -1 if x<0 else 1
##        x*=sign
##        y=0
##        while x!=0:
##            y=y*10+x%10
##            x=x/10
##        return y*sign

##        sign=-1 if x<0 else 1
##        x*=sign
##        lx=[]
##        while x!=0:
##            lx.append(x%10)
##            x=x/10
##
##        x=0
##        for y in lx:
##            x=10*x+y
##        return x*sign
        
x=-123
print(Solution().reverse(x))
        
