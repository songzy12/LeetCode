class Solution(object):
    
    def __init__(self):
        self.a = {'A':0, 'T':1, 'C':2, 'G':3}
        self.i = ['A', 'T', 'C', 'G']

    def atoi(self, s):
        ans = 0
        for i in range(10):
            ans += self.a[s[i]]*(1<<(2*i))
        return ans

    def itoa(self, n):
        ans = ''
        for i in range(10):
            ans = ans + self.i[n%4]
            n /= 4
        return ans

    def findRepeatedDnaSequences(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        if len(s) < 10:
            return []
        m = {}
        temp = self.atoi(s[:10])
        m[temp] = 1
        for i in range(10, len(s)):
            temp //= 4
            temp += self.a[s[i]]*(1<<18)
            m[temp] = m.get(temp, 0) + 1
        ans = []
        for key in m:
            if m[key] > 1:
                ans += [self.itoa(key)]
        return ans
        
s = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"
print Solution().findRepeatedDnaSequences(s)
