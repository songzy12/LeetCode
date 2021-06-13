class Solution(object):
    def isAdditiveNumber(self, num):
        """
        :type num: str
        :rtype: bool
        """
        
        len_i = len(num) // 2
        for i in range(1, len_i + 1):
            len_j = min(len(num) - i // 2, len(num) - 2 * i)
            for j in range(1, len_j + 1):
                if self.check(num, i, j):
                    return True
        return False
    
    def check(self, num, i, j):
        if num[0] == '0' and i > 1: # '1023', 101
            return False
        if not num[i+j:]:
            return True
        res = str(int(num[:i])+int(num[i:i+j]))
        if num[i+j:].startswith(res):
            return self.check(num[i:], j, len(res))
        else:
            return False

print Solution().isAdditiveNumber("112358")
print Solution().isAdditiveNumber("199100199")
print Solution().isAdditiveNumber("1023")
print Solution().isAdditiveNumber("101")
