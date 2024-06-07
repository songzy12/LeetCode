class Solution:
    def floodFill(self, image, sr, sc, newColor):
        """
        :type image: List[List[int]]
        :type sr: int
        :type sc: int
        :type newColor: int
        :rtype: List[List[int]]
        """
        if not image:
            return image
        
        visited = [[False for i in range(len(image[0]))] for j in range(len(image))]

        def bfs(x, y):
            visited[x][y] = True
            ds = [[-1, 0], [1, 0], [0, -1], [0, 1]]
            for dx, dy in ds:
                if 0 <= x + dx < len(image) and 0 <= y + dy < len(image[0]) and \
                   image[x+dx][y+dy] == image[x][y] and not visited[x+dx][y+dy]:
                    bfs(x+dx, y+dy)

        bfs(sr, sc)

        for i in range(len(image)):
            for j in range(len(image[0])):
                if visited[i][j]:
                    image[i][j] = newColor
        return image

image = [[1,1,1],[1,1,0],[1,0,1]]
sr = 1
sc = 1
newColor = 2

Solution().floodFill(image, sr, sc, newColor)

for row in image:
    print(row)
            
        
