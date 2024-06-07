class Solution:

    def decodeAtIndex(self, S, K):
        """
        :type S: str
        :type K: int
        :rtype: str
        """
        import string
        length = 0
        last_c = ''
        for i, c in enumerate(S):
            if c in string.digits:
                if K <= length * int(c):
                    if K % length == 0:
                        return last_c
                    return self.decodeAtIndex(S[:i], K % length)
                else:
                    length *= int(c)
            else:
                last_c = c
                length += 1
                if K == length:
                    return c

S = "a2345678999999999999999"
K = 1
print(Solution().decodeAtIndex(S, K))
