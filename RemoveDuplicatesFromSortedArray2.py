class Solution:
    # @param A a list of integers
    # @return an integer
    def removeDuplicates(self, A):
        count=1
        index=0
        while index<len(A):
            if index+1 < len(A) and A[index+1]==A[index]:
                count+=1
                index+=1
            if count==2:
                while index+1<len(A) and A[index+1]==A[index]:
                    A.remove(A[index])
                count=1
            index+=1
        return index

A=[]
print(Solution().removeDuplicates(A))
# return 5, A=[1,1,2,2,3]
