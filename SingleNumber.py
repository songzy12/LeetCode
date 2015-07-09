class Solution:
    # @param A, a list of integer
    # @return an integer
    def singleNumber(self, A):
        from functools import reduce
        # awsome!!!
        return reduce(lambda x,y:x^y,A)
            


##        # or we can use operator.xor
##        import operator
##        return reduce(operator.xor,A)

##        # dcit use extra space 
##        d={}
##        for i in A:
##            # d.get(i,0) if d[i] does not exist, return 0
##            d[i]=d.get(i,0)+1
##        for x in d:
##            if d[x]==1:
##                return x

        
##        # sort use extra time
##        A.sort()
##        i=iter(A)
##        while True:
##        # i.next() may raise StopItertion Exception
##            try:
##                x=i.next()
##                y=i.next()
##                if x!=y:
##                    break
##            except StopIteration:
##                break
##        return x


A=[1,2,1]
print (Solution().singleNumber(A))
