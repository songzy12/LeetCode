# https://leetcode.com/contest/weekly-contest-76/problems/find-eventual-safe-states/

from heapq import heappush, heappop
class Solution:
    def eventualSafeNodes(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: List[int]
        """
        from collections import defaultdict
        
        in_ = defaultdict(list)
        out_degree = []
        m_out_degree = {}

        for i, edge in enumerate(graph):
            heappush(out_degree, [len(edge), i])
            m_out_degree[i] = len(edge)
            for t in edge:
                in_[t].append(i)

        cnt = defaultdict(int)
        
        ans = []
        visited = set()
        
        while out_degree:
            d, cur = heappop(out_degree)
            if cur in visited: # NOTE: this is even better than a for loop
                continue
            visited.add((d, cur))
            
            if d - cnt[cur] != 0:
                break

            ans.append(cur)
            
            for node in in_[cur]:
                m_out_degree[node] -= 1
                heappush(out_degree, [m_out_degree[node], node])
                
        return sorted(ans)

graph = [[1,2],[2,3],[5],[0],[5],[],[]]

# TLE
print(Solution().eventualSafeNodes(graph))
        
