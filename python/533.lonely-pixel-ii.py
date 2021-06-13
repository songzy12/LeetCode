class Solution(object):
    def findBlackPixel(self, picture, N):
        """
        :type picture: List[List[str]]
        :type N: int
        :rtype: int
        """
        if not picture:
            return 0
        rows = [0 for i in range(len(picture))]
        columns = [0 for j in range(len(picture[0]))]
        
        for i in range(len(picture)):
            for j in range(len(picture[0])):
                if picture[i][j] == 'B':
                    rows[i] += 1
                    columns[j] += 1
        # print rows
        # print columns
        
        checked = [False for j in range(len(picture[0]))]
        ans = 0
        for i in range(len(picture)):
            if rows[i] != N:
                continue
            for j in range(len(picture[0])):
                if picture[i][j] != 'B':
                    continue
                if columns[j] != N:
                    continue
                if checked[j]:
                    continue

                def check(j, row):
                    temp = 0
                    for i in range(len(picture)):
                        if picture[i][j] != 'B':
                            continue
                        # check what is exactly the same
                        # if rows[i] != N:
                        if picture[i] != row:                            
                            return 0
                        temp += 1
                    return temp

                ans += check(j, picture[i])
                checked[j] = True
        return ans

picture = ["WBWBBW","WBWBBW","WBWBBW","WWBWBW"]
N = 3

picture = ["WBBWWBWWWWWBBWW", # 5
           "WBBWWBWWWWWBBWW", # 5
           "WWWWWBBBWBWWWWB", # 5
           "WWBWBWWWWBBWBWW", # 5
           "WBBWWBWWWWWBBWW", # 5
           "WWBWBWWWWBBWBWW", # 5
           "WWBWBWWWWBBWBWW", # 5
           "WWBWBWWWWBBWBWW"] # 5
N = 5 # expected 0

print Solution().findBlackPixel(picture, N)
