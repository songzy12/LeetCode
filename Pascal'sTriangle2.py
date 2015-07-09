class Solution:
    # @return a list of integers
    def getRow(self, rowIndex):
        if rowIndex==0:
            return []
        l=[[1]]
        for i in range(1,rowIndex+1):
            tmp=[1]
            for j in range(1,i):
                tmp.append(l[i-1][j-1]+l[i-1][j])
            tmp.append(1)
            l.append(tmp)
        return l[rowIndex]
        

rowIndex=3
print(Solution().getRow(rowIndex))
