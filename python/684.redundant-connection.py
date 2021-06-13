class Solution(object):
    def findRedundantConnection(self, edges):
        """
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        father = {}

        def find(node):
            while father[node] != node:
                father[node] = father[father[node]]
                node = father[node]
            return node

        
        
        for u, v in edges:
            if u not in father and v not in father:
                father[u] = father[v] = min(u, v)
                continue
            if u not in father:
                father[u] = father[v]
                continue
            if v not in father:
                father[v] = father[u]
                continue

            fu = find(u)
            fv = find(v)
            if fu == fv:
                return [u, v]

            if fu < fv:
                father[fv] = father[fu]
            else:
                father[fu] = father[fv]
            

edges = [[1,2],[4,2],[3,4],[1,3]]
print Solution().findRedundantConnection(edges)
            
