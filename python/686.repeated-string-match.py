class Solution(object):
    def repeatedStringMatch(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: int
        """
        A_ = A
        while B not in A_:
            if len(A_) < len(A) + len(B):
                A_ += A
            else:
                return -1
        return len(A_) / len(A)

A = "abcd"
B = "cdabcdab"
print Solution().repeatedStringMatch(A, B)
        
                
