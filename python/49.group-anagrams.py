class Solution:
    # @param {string[]} strs
    # @return {string[]}
    def anagrams(self, strs):
        result = []
        m = {}
        for s in strs:
            a = [0 for i in range(26)]
            for t in s:
                a[ord(t)-ord('a')]+=1
            if tuple(a) in m:
                m[tuple(a)].append(s)
            else:
                m[tuple(a)] = list((s,))
        for s in m:
            if len(m[s])>=2:
                result += list(m[s])
        return result

print(Solution().anagrams(['ab','ba','c']))
                    
