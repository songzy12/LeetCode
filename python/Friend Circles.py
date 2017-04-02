class Solution(object):
    def findCircleNum(self, M):
        """
        :type M: List[List[int]]
        :rtype: int
        """
        if not M or not M[0]:
            return 0
        
        visited = [False for i in range(len(M))]
        count = 0
        for i in range(len(M)):
            if visited[i]:
                continue
            count += 1
            def bfs(i):
                q = [i]
                while q:
                    top = q.pop(0)
                    if visited[top]:
                        continue
                    visited[top] = True
                    for j in range(len(M)):
                        if M[top][j] and not visited[j]:
                            q += [j]
                return
            bfs(i)
        return count

if __name__ == '__main__':
    M = [[1,1,0],
         [1,1,1],
         [0,1,1]]
    print Solution().findCircleNum(M)
                
        
        
