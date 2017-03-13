class Solution(object):
    def findLonelyPixel(self, picture):
        """
        :type picture: List[List[str]]
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
        ans = 0           
        for i in range(len(picture)):
            for j in range(len(picture[0])):
                ans += picture[i][j] == 'B' and \
                       rows[i] == 1 and \
                       columns[j] == 1
        return ans
