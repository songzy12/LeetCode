# https://leetcode.com/contest/weekly-contest-64/problems/open-the-lock/
class Solution:
    def openLock(self, deadends, target):
        """
        :type deadends: List[str]
        :type target: str
        :rtype: int
        """

        # we can construct a graph and use BFS

        
        deadends = set(deadends)
        length = 4

        start = "0" * length
        # NOTE: corner case
        if start in deadends:
            return -1
        
        q = [(start, 0)]
        visited = set([start])
        
        while q:
            s, step = q.pop(0)
            if s == target:
                return step
            
            for i in range(length):
                ch = s[i]
                for ne in [(int(ch)+1) % 10, (int(ch)-1+10) % 10]:
                    cur = s[:i] + str(ne) + s[i+1:]
                    if cur in deadends:
                        continue
                    if cur in visited:
                        continue
                    visited.add(cur)
                    q.append((cur, step+1))
        return -1

deadends = ["0000"]
target = "8888"
print(Solution().openLock(deadends, target))
        
