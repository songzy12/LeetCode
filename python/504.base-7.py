class Solution(object):
    def convertTo7(self, num):
        """
        :type num: int
        :rtype: str
        """
        if not num:
            return '0'
        flag = num < 0
        num = abs(num)
        ans = ''
        while num:
            ans += str(num % 7)
            num /= 7
        return ('-' if flag else '')+ ans[::-1]

num = -7
print Solution().convertTo7(num)
