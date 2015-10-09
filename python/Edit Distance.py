class Solution:
    # @param {string} word1
    # @param {string} word2
    # @return {integer}
    def minDistance(self, word1, word2):
        self.d = [[-1 for j in range(len(word2)+1)] for i in range(len(word1)+1)]
        # d[i][j] for the distance of word1[:i], word2[:j]
        return self.dp(len(word1), len(word2), word1, word2)
    def dp(self, i, j, word1, word2):
        if self.d[i][j] != -1:
            return self.d[i][j]
        if i == 0:
            self.d[i][j] = j
        elif j == 0:
            self.d[i][j] = i
        elif word1[i-1] == word2[j-1]:
            self.d[i][j] = self.dp(i-1,j-1,word1,word2)
        else:
            self.d[i][j] = min(self.dp(i-1,j-1,word1,word2), self.dp(i-1,j,word1,word2), self.dp(i,j-1,word1,word2))+1
            # replace, delete, insert
        return self.d[i][j]

word1 = 'ab'
word2 = 'bcasda'
print(Solution().minDistance(word1, word2))
        
