class Solution:
    def maxChunksToSorted(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        cnt = [0 for i in range(len(arr))]
        for i, x in enumerate(arr):
            for t in range(max(x, i), len(arr)):
                cnt[t] += 1
            #print(cnt)
        
        res = 0
        for i, x in enumerate(cnt):
            if i + 1 == x:
                res += 1
        return res

arr = [4,3,2,1,0]
print (Solution().maxChunksToSorted(arr))
        
