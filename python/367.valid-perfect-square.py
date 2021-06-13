class Solution(object):
    def isPerfectSquare(self, num):
        """
        :type num: int
        :rtype: bool
        """
        guess = num * 1.0 / 2
        delta = 1
        while delta > 0.3:
            tmp = 0.5 * (num / guess + guess)
            delta = abs(tmp - guess)
            guess = tmp
        guess = round(guess)
        return guess * guess == num
        
for num in range(1, 16):
    print num, Solution().isPerfectSquare(num)
