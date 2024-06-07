class Solution(object):
    def reverseStr(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        ans = ''
        for i in range(0, len(s),k):
            ans += s[i:i+k][::-1] if (i / k) % 2 == 0 else s[i:i+k]
        return ans

if __name__ == '__main__':
    s = 'abcdef'
    k = 3
    print Solution().reverseStr(s, k)
