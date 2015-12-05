class Solution(object):
    def findMinHeightTrees(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        if n == 1:
            return [0]

        degree = {}
        nodes = {}
        for i in range(n):
            degree[i] = 0
            nodes[i] = []
        for u, v in edges:
            degree[u] += 1
            degree[v] += 1
            nodes[u] += v,
            nodes[v] += u,
            
        q = [i for i in range(n)]
        pre = [i for i in range(n) if degree[i] == 1]
        while len(q) > 2:
        # middle point of longest path, at most 2 nodes
            this = []
            for i in pre:
            # for i in q
                q.remove(i)
                for j in nodes[i]:
                    if j in q:
                        degree[j] -= 1
                        if degree[j] == 1:
                            this += j,
            pre = this
        return q

n = 6
edges = [[0, 3], [1, 3], [2, 3], [4, 3], [5, 4]]
print Solution().findMinHeightTrees(n, edges)
