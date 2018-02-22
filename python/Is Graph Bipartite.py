class Solution:
    def isBipartite(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: bool
        """
        color = {}

        # NOTE: there may be multiple connected components
        for i in range(len(graph)):
            if i in color:
                continue
            q = [i]
            color[i] = 0
            while q:
                cur = q[0]
                q.pop(0)
                cur_color = color[cur]
                
                for v in graph[cur]:
                    if v not in color:
                        q += v,
                        color[v] = 1 - cur_color
                    elif color[v] != 1 - cur_color:
                        return False
                    else:
                        continue
        return True

graph = [[], [2,4,6],[1,4,8,9],[7,8],[1,2,8,9],[6,9],[1,5,7,8,9],[3,6,9],[2,3,4,6,9],[2,4,5,6,7,8]]
print(Solution().isBipartite(graph))
