class Solution(object):
    def checkPerfectNumber(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num <= 1:
            return False
        import math
        def get_divisors(num):
            res = [1]
            for i in range(2, int(math.sqrt(num)) + 1):
                if num % i == 0:
                    res += [i, num / i] if i * i != num else [i]
            return res
        
        return num == sum(get_divisors(num))
