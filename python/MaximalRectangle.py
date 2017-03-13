class Solution:
    #@param matrix, a list of lists of l length string
    #@return an integer

    # at first I enumerate all the rectangles
    # check whether it is filled or not
    # then return max
    # but time limit exceeded.
    
    # there is a better solution in the discuss section
    # remember to check it when you get spare time >_<

    def maximalRectangle(self, matrix):
        # this is the same as top voted solution
        # except that this keeps a fixed right, then search up and down
        # top voted solution keeps a fixed height, use dp for left and right
        if not matrix:
            return 0
        # here not bother to use else:
        rows=len(matrix)
        columns=len(matrix[0])

        # inorder to partially assign
        for i in range(rows):
            matrix[i]=list(matrix[i])

        # try to use xrange if no need to return a list
        for i in range(rows):
            current=0
            for j in range(columns-1,-1,-1):
                if matrix[i][j]=='1':
                    current +=1
                    # just update matrix[i][j] to save space
                else:
                    current=0
                matrix[i][j]=current
        # after this, contains # continuous 1's to its right
        
        max_area=0
        for i in range(rows):
            for j in range(columns):
                temp_area=matrix[i][j]
                if temp_area==0:
                    continue
                # do not bother to use else:
                k=1
                #search down
                while i+k <rows:
               
                    if matrix[i+k][j]>=matrix[i][j]:
                        temp_area+=matrix[i][j]
                    else:
                        break
                    k+=1
                k=1
                #search up
                while i-k>=0:
                    if matrix[i-k][j]>=matrix[i][j]:
                        temp_area+=matrix[i][j]
                    else:
                        break
                    k+=1
                max_area=max(max_area, temp_area)
        return max_area

for matrix in [],["0"],["1"],["01","10"],["00","11"]:
    print(Solution().maximalRectangle(matrix))
