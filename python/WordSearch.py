class Solution:
    # @param board, a list of lists of 1 length string
    # @param word, a string
    # @return a boolean

    d=[]
    def exist(self, board, word):
        if len(board)==0 or len(board[0])==0:
            return False
        self.d=[[0 for j in range(len(board[0]))] for x in range(len(board))]
        for i in range(len(board)):
            for j in range(len(board[0])):
                if(self.auxExist(board,word,i,j,0)):
                    return True
        return False
    def auxExist(self, board, word, i, j, n):
        # instead of passing a list, we pass the index
        if n==len(word):
            return True
        if i<0 or i==len(board) or j<0 or j==len(board[0]) or \
           self.d[i][j]==1 or board[i][j]!=word[n]:
            return False
        self.d[i][j]=1
        if (self.auxExist(board, word, i-1, j,n+1)) or\
           (self.auxExist(board, word, i+1, j,n+1)) or\
           (self.auxExist(board, word, i, j-1,n+1)) or\
           (self.auxExist(board, word, i, j+1,n+1)):
            # instead of initializing each time, we recover the modified bit
            self.d[i][j]=0
            return True
        self.d[i][j]=0
        return False


##    # TLE
##    d=[]
##    # use self.d to refer to the global variance
##    def exist(self, board, word):
##        # if board=[['ABCE'],['SFCS'],['ADEE']]
##        # board[0]=['ABCE'] len(board[0])=1
##        # board[0][0]='ABCE', len(board[0][0])=4
##        if len(board)==0 or len(board[0])==0:
##            return False
##        for i in range(len(board)):
##            for j in range(len(board[0])):
##                if board[i][j]==word[0]:
##                    # remeber to recover d after one failed search
##                    # and notice how to initial 2d list
##                    self.d=[[0 for j in range(len(board[0]))]\
##                            for x in range(len(board))]
##                    if(self.auxExist(board,word,i,j)):
##                        return True
##        return False
##
##    def auxExist(self, board, word, i, j):
##        if board[i][j]!=word[0]:
##            return False
##        # value need to be modified here 
##        self.d[i][j]=1
##        if len(word)==1:
##            return True
##        word=word[1:]
##        return (False if i==0 else self.auxExist(board, word, i-1, j))or\
##               (False if i==len(board)-1 else self.auxExist(board, word, i+1, j))or\
##               (False if j==0 else self.auxExist(board, word, i, j-1))or\
##               (False if j==len(board[0])-1 else self.auxExist(board, word, i, j+1))


##board=['ABCE',
##       'SFCS',
##       'ADEE']
##for word in ['ABCCED','SEE','ABCB']:
board=['CAA',
       'AAA',
       'BCD']
word='AAB'
print(Solution().exist(board,word))
