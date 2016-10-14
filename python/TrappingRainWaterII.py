# Given an m x n matrix of positive integers representing the height of each unit cell in a 2D elevation map, 
# compute the volume of water it is able to trap after raining. 

class Solution(object):
    def trapRainWater(self, heightMap):
        """
        :type heightMap: List[List[int]]
        :rtype: int
        """
        if not heightMap or len(heightMap) < 3:
            return 0
        visited = [[False for i in range(len(heightMap[0]))] for j in range(len(heightMap))]
        heap = [(heightMap[i][0], i, 0) for i in range(len(heightMap))] + \
               [(heightMap[i][-1], i, len(heightMap[0]) - 1) for i in range(len(heightMap))] + \
               [(heightMap[0][j], 0, j) for j in range(len(heightMap[0]))] + \
               [(heightMap[-1][j], len(heightMap) - 1, j) for j in range(len(heightMap[0]))]
        
        for i in range(len(heightMap)):
            visited[i][0] = visited[i][-1] = True
        for i in range(len(heightMap[0])):
            visited[0][i] = visited[-1][i] = True
            
        import heapq
        heapq.heapify(heap)
        res = 0
        while heap:
            hegiht, i, j = heapq.heappop(heap)
            for x, y in [(0, -1), (0, 1), (1, 0), (-1, 0)]:
                if 0 <= i+x < len(heightMap) and 0 <= j+y < len(heightMap[0]) and \
                   not visited[i+x][j+y]:
                    temp = max(heightMap[i+x][j+y], heightMap[i][j]) - heightMap[i+x][j+y]
                    res += temp 
                    visited[i+x][j+y] = True
                    heightMap[i+x][j+y] = max(heightMap[i+x][j+y], heightMap[i][j]) # to replace 
                    heapq.heappush(heap, (heightMap[i+x][j+y],i+x,j+y))
        return res
            
        
heightMap = [[12,13,1,12],
             [13,4,13,12],
             [13,8,10,12],
             [12,13,12,12],
             [13,13,13,13]]
print Solution().trapRainWater(heightMap)

# use priority queue, put the border into that queue 
# then shrink inward from the lowerest one