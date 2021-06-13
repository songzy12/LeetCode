class Solution(object):
    def constructArray(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[int]
        """
        res = []
        head, tail = 1, k + 1
        while head < tail:
            res.extend([head, tail])
            head += 1
            tail -= 1
        if head == tail:
            res.append(head)
        res.extend(range(k + 2,n + 1))
        return res

n = 7
k = 3
print Solution().constructArray(n, k)
