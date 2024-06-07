class Solution:
    # @param {integer[][]} matrix
    # @return {integer[]}
    def spiralOrder(self, matrix):
        if not matrix or not matrix[0]:
            return []
        m = min(len(matrix), len(matrix[0]))
        n_layer = (m+1)//2
        ans = []
        for i in range(n_layer):
            ans += self.getLayer(i, matrix)
        return ans
    def getLayer(self, n, matrix):
        l, r, t, b = n, len(matrix[0])-1-n, n, len(matrix)-1-n
        #print(l,r,t,b)
        if l == r and t == b:
            return [matrix[l][t]]
        if l == r:
            return [matrix[i][l] for i in range(t, b+1)]
        if t == b:
            return matrix[t][l:r+1]
        ans = []
        for i in range(l, r):
            ans += [matrix[t][i]]
        for i in range(t, b):
            ans += [matrix[i][r]]
        for i in range(r, l, -1):
            ans += [matrix[b][i]]
        for i in range(b, t, -1):
            ans += [matrix[i][l]]
        #print(ans)
        return ans

matrix = [[1,2,3],
          [4,5,6]]
print(Solution().spiralOrder(matrix))
