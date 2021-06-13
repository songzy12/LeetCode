class Solution(object):
    def findNthDigit(self, n):
        """
        :type n: int
        :rtype: int
        """
        # n < 2**31
        width = 1
        while n > width * (10**width - 10**(width-1)):
            n -= width * (10**width - 10**(width-1))
            width += 1
        # now n is in the block of width        
        start = 10**(width-1) # start is the next number
        hold = start + (n - 1)// width # same result for n = 1 or width 
        return int(str(hold)[(n - 1) % width])
    
n = 10
print Solution().findNthDigit(n)

# first thought: 1*9, 2*90, 3*900, ..., 
# n * (\underbrace{9..9}_{n} - \underbrace{9..9}_{n-1}) = n * (10**n - 10**(n-1)).

# after we know n, we abstract 10**(n-1) one by one, to get the first digit.
# then abstract 10**(n-2) one by one, to get the second digit.
# no way

# How do we get the number that will hold the digit?
# It will be start + (n - 1) // size
# (we use n - 1 because we need zero-based index).
# Once we have that number, we can get the n - 1 % size-th digit of that number,
# and that will be our result.

