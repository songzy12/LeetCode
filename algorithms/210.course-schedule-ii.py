class Solution(object):
    def findOrder(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """
        degree = [0 for i in range(numCourses)]
        m = [[] for i in range(numCourses)]
        for edge in prerequisites:
            m[edge[1]] += edge[0],
            degree[edge[0]] += 1
        q = []
        for i in range(numCourses):
            if degree[i] == 0:
                q += i,
        ans = []
        while q:
            t = q.pop(0)
            ans += t,
            for node in m[t]:
                degree[node] -= 1
                if not degree[node]:
                    q += node,
        for i in degree:
            if i:
                return []
        return ans

numCourses, prerequisites = 4, [[1,0],[2,0],[3,1],[3,2]]
print Solution().findOrder(numCourses, prerequisites)
