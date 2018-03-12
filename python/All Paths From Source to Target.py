class Solution:
    def allPathsSourceTarget(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: List[List[int]]
        """
        prev = {}
        queue = [0]
        
        while queue:
            next_queue = []
            while queue:
                cur = queue.pop(0)
                for node in graph[cur]:
                    if node not in prev:
                        prev[node] = set()
                    prev[node].add(cur)
                    next_queue.append(node)
            queue = next_queue

        prev[0] = []

        res = []
        def get_path(node):
            if not prev[node]:
                return [[node]]

            ans = []
            for last in prev[node]:
                ans += [x + [node] for x in get_path(last)]
            return ans
        return get_path(len(graph)-1)

graph = [[1,2], [3], [3], [4], []]
print(Solution().allPathsSourceTarget(graph))
        
        
