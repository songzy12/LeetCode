class Solution(object):
    def selfDividingNumbers(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: List[int]
        """
        def check(n):
            t = n
            while t:
                a = t % 10
                if not a:
                    return False
                if n % a:
                    return False                
                t /= 10
            return True
        return list(filter(check, range(left, right+1)))

left = 1
right = 22
print Solution().selfDividingNumbers(left, right)
