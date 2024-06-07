class Solution(object):
    def frequencySort(self, s):
        """
        :type s: str
        :rtype: str
        """
        import collections
        c = collections.Counter(s)
        bucket = [[] for i in range(len(s)+1)]
        for k, v in c.items():
            bucket[v].append((k, v))
        return "".join(["".join([k*v for k,v in t]) for t in bucket[::-1]])

s = "cccabb"
print Solution().frequencySort(s)
        
