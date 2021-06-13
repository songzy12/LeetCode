class Solution:
    def reorganizeString(self, S):
        """
        :type S: str
        :rtype: str
        """
        len_S = len(S)
        import string, heapq
        c = []
        for x in string.ascii_lowercase:
            temp = [-S.count(x), x]
            if temp[0]:
                heapq.heappush(c, temp)

        if not c:
            return ""
        
        res = ""
        pre = heapq.heappop(c)
        pre[0] += 1
        res += pre[-1]
        
        while c:
            cur = heapq.heappop(c)
            cur[0] += 1
            res += cur[-1]
            
            if pre[0]:
                heapq.heappush(c, pre)
            pre = cur
            
        if pre[0]:
            return ""
        return res
        

S = "vvvlo"
print (Solution().reorganizeString(S))
