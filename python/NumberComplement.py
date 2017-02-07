class Solution(object):
    def findComplement(self, num):
        """
        :type num: int
        :rtype: int
        """
        return int(''.join(map(lambda x: '0' if x == '1' else '1', bin(num)[2:])),2)
##        i = 1
##        while i <= num:
##            i = i << 1
##        return (i - 1) ^ num
