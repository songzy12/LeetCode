# Given an integer n, return 1 - n in lexicographical order.
# For example, given 13, return: [1,10,11,12,13,2,3,4,5,6,7,8,9].

class Solution(object):
    def lexicalOrder(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        top = 1
        while top * 10 <= n:
            top *= 10
        def mycmp(a, b, top=top):
            while a < top: a *= 10
            while b < top: b *= 10
            return -1 if a < b else b < a
        return sorted(xrange(1, n+1), mycmp)

# first thought: no thought
# solution 1: stable sort, the comparison function left-shift each number first
# solution 2: combine each number with a left-aligned version, then extract
# solution 3: 
