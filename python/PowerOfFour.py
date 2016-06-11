class Solution(object):
    def isPowerOfFour(self, num):
        """
        :type num: int
        :rtype: bool
        """
        # there is only one 1 and it is located at odd position
        return num > 0 and num & (num - 1) == 0 and num & 0x55555555 == num
        
        if num <= 0:
            return False
        while num:
            if num & 3 and num != 1:
                return False
            num >>= 2
        return True

num = 17
print Solution().isPowerOfFour(num)
