class Solution(object):
    def complexNumberMultiply(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        def parse(a):
            a = a.split('+')
            return map(int, [a[0], a[-1][:-1]])
        ar, ai = parse(a)
        br, bj = parse(b)
        return str(ar*br-ai*bj)+"+"+str(ar*bj+ai*br)+"i"

if __name__ == '__main__':
    a, b = "1+-1i", "1+-1i"
    print Solution().complexNumberMultiply(a, b)
        
