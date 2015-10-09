class Solution:
    # @param A, a list of integers
    # @param target, an integer to be inserted
    # @return integer
    def searchInsert(self, A, target):
        if len(A)==0:
            return 0
        i=0
        while  i<len(A) and A[i]<target:
            i+=1
        return i
    
A=[1,3,5,6]
for target in 5,2,7,0:
    print(Solution().searchInsert(A,target))
