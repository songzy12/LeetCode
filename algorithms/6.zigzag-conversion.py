class Solution:
    # @return a string
    def convert(self, s, nRows):
        length=len(s)
        table=['' for i in range(nRows)]
        index=0
        while index<length:
            for i in range(nRows):
                if index==length:
                    break
                table[i]=table[i]+s[index]
                index=index+1
            for i in range(nRows-2,0,-1):
                if index==length:
                    break
                table[i]=table[i]+s[index]
                index=index+1
        return ''.join(table)
            
##        if nRows==1:
##            return s
##        if nRows==2:
##            return ''.join([s[i] for i in range(len(s)) if i%2==0]+
##                           [s[i] for i in range(len(s)) if i%2==1])
##        nColumns = len(s)//(2*nRows-2)*2 + 2
##        table = [[0 for i in range(nColumns)] for j in range(nRows)]
##        length = len(s)
##        for j in range(nColumns):
##            for i in range(nRows):
##                if j%2==0 and i+j//2*(2*nRows-2) < length:
##                    table[i][j]=s[i+j//2*(2*nRows-2)]
##                if (j%2==1 and i!=0 and i!=nRows-1 and
##                    j//2*(2*nRows-2)+2*nRows-2-i<length):
##                    table[i][j]=s[j//2*(2*nRows-2)+2*nRows-2-i]
##        for j in table[1:]:
##            table[0].extend(j)
##        return ''.join([i for i in table[0] if i!=0])

s='ABCD'
nRows=2
s='A'
nRows=3
s="PAYPALISHIRING"
nRows=3
print(Solution().convert(s, nRows))
# "PAHNAPLSIIGYIR"
