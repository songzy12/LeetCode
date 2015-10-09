class Solution:
    # @return a list of lists of integers
    def generate(self, numRows):
        if numRows==0:
            return []
        l=[[1]]
        for i in range(1,numRows):
            tmp=[1]
            for j in range(1,i):
                tmp.append(l[i-1][j-1]+l[i-1][j])
            tmp.append(1)
            l.append(tmp)
        return l
        

numRows=5
print(Solution().generate(numRows))
