##class Solution:
##    def findCheapestPrice(self, n, flights, src, dst, K):
##        """
##        :type n: int
##        :type flights: List[List[int]]
##        :type src: int
##        :type dst: int
##        :type K: int
##        :rtype: int
##        """
##        # NOTE: float('inf')
##        dis = [float('inf')] * n
##        pre = [float('inf')] * n
##        dis[src] = pre[src] = 0
##
##        for i in xrange(K+1):
##            for u, v, w in flights:
##                dis[v] = min(dis[v], pre[u] + w)
##            pre = dis
##
##        return dis[dst] if dis[dst] < float('inf') else -1

# Dijkstra's Algorithm
class Solution(object):
    def findCheapestPrice(self, n, flights, src, dst, K):
        import collections, heapq
        graph = collections.defaultdict(dict)
        for u, v, w in flights:
            graph[u][v] = w

        best = {}
        pq = [(0, 0, src)]
        while pq:
            cost, k, place = heapq.heappop(pq)
            if k > K+1 or cost > best.get((k, place), float('inf')): continue
            if place == dst: return cost

            for nei, wt in graph[place].items():
                newcost = cost + wt
                if newcost < best.get((k+1, nei), float('inf')):
                    heapq.heappush(pq, (newcost, k+1, nei))
                    best[k+1, nei] = newcost

        return -1
        
##n = 3
##edges = [[0,1,100],[1,2,100],[0,2,500]]
##src = 0
##dst = 2
##k = 1
##
##n = 3
##edges = [[0,1,100],[1,2,100],[0,2,500]]
##src = 0
##dst = 2
##k = 0

n = 10
edges = [[3,4,4],[2,5,6],[4,7,10],[9,6,5],[7,4,4],[6,2,10],[6,8,6],[7,9,4],[1,5,4],[1,0,4],[9,7,3],[7,0,5],[6,5,8],[1,7,6],[4,0,9],[5,9,1],[8,7,3],[1,2,6],[4,1,5],[5,2,4],[1,9,1],[7,8,10],[0,4,2],[7,2,8]]
src = 6
dst = 0
k = 7

print(Solution().findCheapestPrice(n, edges, src, dst,k))

# NOTE: up to k stops, rather than k rounds of Floyd
