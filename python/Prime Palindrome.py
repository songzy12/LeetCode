class Solution(object):

    def primePalindrome(self, N):
        """
        :type N: int
        :rtype: int
        """
        def isPrime(n):
            if n == 1:
                return False
            for t in range(2, int(n ** 0.5) + 1):
                if n % t == 0:
                    return False
            return True

        def isPalindrome(n):
            return str(n)[::-1] == str(n)

        def nextPalindrome(n):
            str_n = str(n)
            if len(str_n) % 2 == 0:
                head = str_n[:len(str_n) / 2]
                temp = int(head + head[::-1])
                if temp > n:
                    return temp

                head = str(int(head) + 1)
                temp = int(head + head[::-1])
                return temp
            head = str_n[:len(str_n) / 2 + 1]
            temp = int(head + head[:-1][::-1])
            if temp > n:
                return temp
            head = str(int(head) + 1)
            temp = int(head + head[:-1][::-1])
            return temp

        t = N
        while not isPrime(t) or not isPalindrome(t): # NOTE: here we need to check both
            t = nextPalindrome(t)
        return t

N = 8  # 9957599
print(Solution().primePalindrome(N))
