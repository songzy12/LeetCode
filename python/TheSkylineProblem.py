class Solution:
    # @param {integer[][]} buildings
    # @return {integer[][]}
    def getSkyline(self, buildings):
        n = len(buildings)
        if n == 0:
            return []
        if n == 1:
            return [[buildings[0][0],buildings[0][2]], [buildings[0][1],0]]
        mid = (n + 1)//2
        left = self.getSkyline(buildings[:mid])
        right = self.getSkyline(buildings[mid:])
        m = len(left)
        n = len(right)
        i = 0
        j = 0
        h1 , h2 = -1, -1
        result = []
        while i < m and j < n:
            if left[i][0] < right[j][0]:
                h1 = left[i][1]
                tmp = [left[i][0], h1] if h1 >= h2 else [left[i][0], h2]
                if result == [] or result[-1][1] != tmp[1]:
                    result.append(tmp)
                i += 1
            elif left[i][0] > right[j][0] :
                h2 = right[j][1]
                tmp = [right[j][0], h2] if h2 >= h1 else [right[j][0], h1]
                if result == [] or result[-1][1] != tmp[1]:
                    result.append(tmp)
                j += 1
            else:
                h1=left[i][1]
                h2=right[j][1]
                tmp =[right[j][0], h2] if h2 >= h1 else [right[j][0], h1]
                if result==[] or result[-1][1]!=tmp[1]:
                    result.append(tmp)
                i+=1
                j+=1
        while i < m:
            if result==[] or result[-1][1]!=left[i][1]:
                result.append(left[i][:])
            i+=1
        while j < n:    
            if result==[] or result[-1][1]!=right[j][1]:
                result.append(right[j][:])
            j+=1
        return result 

buildings = [[2, 9, 10], [3, 7, 15], [5, 12, 12], [15, 20, 10], [19, 24, 8]]
print(Solution().getSkyline(buildings))
