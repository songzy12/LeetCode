# Given a non-negative integer num represented as a string, 
# remove k digits from the number 
# so that the new number is the smallest possible. 

class Solution(object):
    def removeKdigits(self, num, k):
        """
        :type num: str
        :type k: int
        :rtype: str
        """
        out = []
        for d in num:
            while k and out and out[-1] > d: # if decrease 
                out.pop()
                k -= 1
            out.append(d)
        return ''.join(out[:-k or None]).lstrip('0') or '0' # or

print '123'[:0]

num = "1432219"
k = 3
print Solution().removeKdigits(num, k)

# first thought: check each bit for remove or not, dp

# greedy: remove previous digits if that makes the number smaller
# out[:-k or None], '123'[:0] returns '' while '123'[:None] returns '123'
# out.lstrip('0') or '0', strip the leading '0's while if nothing left return '0'