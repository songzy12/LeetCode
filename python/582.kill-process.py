class Solution(object):
    def killProcess(self, pid, ppid, kill):
        """
        :type pid: List[int]
        :type ppid: List[int]
        :type kill: int
        :rtype: List[int]
        """
        from collections import defaultdict
        m = defaultdict(list)
        for i in range(len(pid)):
            m[ppid[i]].append(pid[i])
        ans = [kill]
        q = [kill]
        while q:
            p = q.pop()
            for s in m[p]:
                ans += s,
                q.append(s)
        return ans

    
        
