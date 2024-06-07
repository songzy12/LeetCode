class Solution:
    # @param {integer} numCourses
    # @param {integer[][]} prerequisites
    # @return {boolean}
    def canFinish(self, numCourses, prerequisites):
        if not prerequisites:
            return True
        deg = [0 for i in range(numCourses)]
        edge = [[] for i in range(numCourses)]
        for e in prerequisites:
            deg[e[1]] += 1
            edge[e[0]] += e[1],
        q = []
        for i in range(len(deg)):
        # for i in deg, list faster than map
            if not deg[i]:
                q += i,
        #print(deg)
        #print(edge)
        while q:
            cur = q.pop(0)
            for i in edge[cur]:
                deg[i] -= 1
                if not deg[i]:
                    q += i,
        #print(deg)
        for i in deg:
            if deg[i]:
                return False
                break
        else:
            return True

print(Solution().canFinish(3, [[1,0],[2,0]]))
