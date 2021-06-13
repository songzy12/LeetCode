class Solution(object):
    def accountsMerge(self, accounts):
        """
        :type accounts: List[List[str]]
        :rtype: List[List[str]]
        """

        from collections import defaultdict
        m = defaultdict(set)

        for i, account in enumerate(accounts):
            for email in account[1:]:
                m[email].add(i)

        
        graph = defaultdict(list)
        for v in m.values():
            
            v = list(v)
            for i in range(len(v)):
                for j in range(i+1, len(v)):
                    graph[v[i]].append(v[j])
                    graph[v[j]].append(v[i])

         
        visited = [False for i in range(len(accounts))]
        result = []

        for i in range(len(accounts)):
            if visited[i]:
                continue

            temp = set()
            q = [i]
            while q:
                cur = q.pop(0)
                
                temp = temp.union(set(accounts[cur][1:]))
                
                for node in graph[cur]:
                    if visited[node]:
                        continue
                    q.append(node)
                    visited[node] = True
                    
            result.append([accounts[i][0]] + sorted(list(temp)))
            visited[i] = True
        return result
        
accounts = [["John", "johnsmith@mail.com", "john00@mail.com"], ["John", "johnnybravo@mail.com"], ["John", "johnsmith@mail.com", "john_newyork@mail.com"], ["Mary", "mary@mail.com"]]
print Solution().accountsMerge(accounts)

        
