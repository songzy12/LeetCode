class Solution:
    # @param A, a list of integer
    # @return an integer
    def singleNumber(self, A):
        # that is awsome!!!
        ones=twos=0
        for i in range(len(A)):
            # first time, not contained in twos, saved in ones
            # fitst time, contained in ones, not saved in twos
            # second time, not contained in twos, cleared in ones
            # second time, not contained in ones, saved in twos
            # third time, contianed in twos, not saved in ones
            # third time, not contianed in ones, cleared in twos
            ones=(ones ^ A[i]) & ~twos
            # not in ones, not in twos, can be saved in ones
            # in ones, will be cleared in ones
            # not in ones, in twos, will not be saved in ones
            twos=(twos ^ A[i]) & ~ones
        return ones
 
##        dict0={}
##        for x in A:
##            if x not in dict0:
##                dict0[x]=1
##            else:
##                dict0[x]+=1
##        for x in dict0:
##            if dict0[x]==1:
##                return x
    

A=[1,2,1,1]
print(Solution().singleNumber(A))
