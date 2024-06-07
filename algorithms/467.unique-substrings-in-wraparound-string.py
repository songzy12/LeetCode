# Your job is to find out how many unique non-empty substrings of p are present in s

class Solution(object):
    def findSubstringInWraproundString(self, p):
        """
        :type p: str
        :rtype: int
        """
        checked = {}
        i = 0
        while i < len(p):
            # start from index i
            j = i + 1
            while j < len(p):
                if ord(p[j]) - ord(p[j-1]) == 1 or (ord(p[j-1]), ord(p[j])) == (ord('z'), ord('a')):
                    j += 1
                else:
                    break
            for t in range(i, j):
                if p[t] in checked and j - t <= checked[p[t]]:
                    continue
                checked[p[t]] = j - t
            i = j
        return sum(checked.values())
            
for p in ["a", "cac", "zab"]:
    print Solution().findSubstringInWraproundString(p)
