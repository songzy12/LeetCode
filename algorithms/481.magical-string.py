class Solution(object):
    def magicalString(self, n):
        """
        :type n: int
        :rtype: int
        """
        a = [1,2,2] # Kolakoski Sequence
        b = [1,2]
        flag = 1
        i_b = len(b)
        i_a = len(a)
        while i_a < n:
            b += a[i_b],
            a += [flag]*a[i_b]
            i_a += a[i_b]
            i_b += 1
            flag = 3 - flag
        return a[:n].count(1)

n = 89999 # TLE
print Solution().magicalString(n)

'''
def magicalString(self, n):
    def gen():
        for x in 1, 2, 2:
            yield x
        for i, x in enumerate(gen()):
            if i > 1:
                for _ in range(x):
                    yield i % 2 + 1
    return sum(x & 1 for x in itertools.islice(gen(), n))
'''
