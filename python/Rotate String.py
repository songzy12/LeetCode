class Solution:
    def rotateString(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: bool
        """
        if len(A) != len(B):
            return False

        if not A and not B:
            return True

        def rotate(A, n):
            return A[n:]+A[:n]
        
        for n in range(len(A)):
            print(n, rotate(A, n))
            if rotate(A, n) == B:
                return True
        return False

A = "abcde"
B = "cdeab"
A = ''
B = ''
print(Solution().rotateString(A, B))
