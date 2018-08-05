class Solution:

    def reachableNodes(self, edges, M, N):
        """
        :type edges: List[List[int]]
        :type M: int
        :type N: int
        :rtype: int
        """
        from collections import defaultdict
        m_edges = defaultdict(dict)

        for u, v, t in edges:
            m_edges[u][v] = t
            m_edges[v][u] = t

        cnt = 1
        q = [(0, M)]

        covered = defaultdict(int)
        visited = defaultdict(int)
        visited[0] = M

        while q:
            u, m = q.pop(0)
            for v in m_edges[u]:
                t = m_edges[u][v]
                # print("%d -> %d: %d" % (u, v, m))
                if t + 1 <= m :
                    if v not in visited:
                        cnt += 1
                    if  m - (t + 1) > visited[v]:
                        q.append([v, m - (t + 1)])
                        visited[v] = m - (t + 1)
                
                if (covered[u,v]+covered[v,u] >= t):
                    continue
                    
                cnt += max(0, min(m, t) - covered[u, v]) - \
                    (max(0, covered[v, u] - (t - min(m, t))))
                # print('cnt: %d' % cnt)
                covered[u, v] = min(m, t)
        return cnt

edges = [[1,2,5],[0,3,3],[1,3,2],[2,3,4],[0,4,1]]
M = 7
N = 5
print(Solution().reachableNodes(edges, M, N))