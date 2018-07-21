# https://leetcode.com/problems/redundant-connection-ii/description/


class Solution:

    def findRedundantDirectedConnection(self, edges):
        """
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        from collections import defaultdict
        from heapq import heappush, heappop

        degrees = defaultdict(int)
        in_degrees = defaultdict(int)
        edges_ = defaultdict(set)
        in_edges_ = defaultdict(set)
        heap = []

        timestamp = {}

        candidate = None

        for i, edge in enumerate(edges):
            u, v = edge
            degrees[u] += 1
            degrees[v] += 1
            in_degrees[v] += 1
            if (in_degrees[v] == 2):
                candidate = v
            edges_[u].add(v)
            edges_[v].add(u)
            in_edges_[v].add(u)
            timestamp[tuple(edge)] = i

        # print('degrees:', degrees)
        for node, degree in degrees.items():
            heappush(heap, (degree, node))

        not_valid = set()
        while True:
            degree, node = heappop(heap)
            if node in not_valid:
                continue
            if degree == 2:
                break
            for v in edges_[node]:
                degrees[v] -= 1
                edges_[v].remove(node)
                if node in in_edges_[v]:
                    in_edges_[v].remove(node)
                heappush(heap, (degrees[v], v))
            edges_[node].clear()
            in_edges_[node].clear()
            not_valid.add(node)

        assert(degree == 2)

        ans = []
        ts = 0

        if candidate:
            for node in in_edges_[candidate]:
                if not ans or ts < timestamp[(node, candidate)]:
                    ans = (node, candidate)
                    ts = timestamp[(node, candidate)]
            return ans

        # print ('edges_:', edges_)
        while edges_[node]:
            edge = edges_[node].pop()
            edges_[edge].remove(node)
            if (edge, node) in timestamp:
                if not ans or timestamp[(edge, node)] > ts:
                    ans = (edge, node)
                    ts = timestamp[(edge, node)]
            else:
                if not ans or timestamp[(node, edge)] > ts:
                    ans = (node, edge)
                    ts = timestamp[(node, edge)]
            node = edge
        return ans


edges = [[1, 2], [2, 3], [3, 4], [4, 1], [1, 5]]
edges = [[1, 2], [1, 3], [2, 3]]
edges = [[4, 1], [1, 5], [4, 2], [5, 1], [4, 3]]
edges = [[2, 1], [6, 3], [5, 8], [3, 5], [6, 9],
         [2, 4], [6, 10], [2, 7], [10, 2], [10, 5]]
edges = [[2, 1], [3, 1], [4, 2], [1, 4]]
print(Solution().findRedundantDirectedConnection(edges))

# 找出那一个环
# 总是会有一个环的
# 这个环会有分叉或者没有分叉

# 如果有入度为 2 的点
# 要删掉的边需要 a. 在环上 b. 是度为 2 的入边

# 如果没有
# 那就删掉环上的任何一个

# 使用 union find 可以大大简化代码
# 遇到环的过程是在 union find 过程中
# 时间戳也不需要