class Solution(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        return num and (num % 9 or 9)
'''
        if not num:
            return 0
        if not num % 9:
            return 9
        return num % 9
‘’‘

'''
        while num//10:
            res = 0
            while num//10:
                res += num%10
                num //= 10
            num += res
        return num
'''

num = 38324
print Solution().addDigits(num)
