class Solution:
    def maxChunksToSorted(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        def preprocess(arr):
            nums = [(x, i) for i, x in enumerate(arr)]
            nums.sort()
            #print(nums)
            for i, t in enumerate(nums):
                arr[t[1]] = i
        preprocess(arr)
        #print(arr)
        visited = [0 for i in range(len(arr))]
        prefix = 0
        res = 0
        for i, x in enumerate(arr):
            visited[x] = 1
            prefix += visited[i]
            if x < i:
                prefix += 1
            if prefix == i+1:
                res += 1
        return res

arr = [2,1,3,4,4]
print (Solution().maxChunksToSorted(arr))
            
                
