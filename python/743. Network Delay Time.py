class Solution:
    def networkDelayTime(self, times, N, K):
        """
        :type times: List[List[int]]
        :type N: int
        :type K: int
        :rtype: int
        """
        d = [-1 for i in range(N+1)]

        d[K] = 0
        q = [K]

        from collections import defaultdict
        edges = defaultdict(list)

        for u, v, w in times:
            edges[u].append([v, w])
        
        while q:
            u = q.pop(0)
            
            for v, w in edges[u]:
                if d[v] == -1 or d[v] > d[u] + w:
                    d[v] = d[u] + w
                    q.append(v)

        
        res = -1
        for n in range(1, N+1):
            if d[n] == -1:
                return -1
            if d[n] > res:
                res = d[n]
        return res

times = [[1,2,1]] # directed
N = 2
K = 2
print(Solution().networkDelayTime(times, N, K))
            
            
        
