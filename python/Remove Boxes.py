class Solution(object):
    def removeBoxes(self, A):
        """
        :type boxes: List[int]
        :rtype: int
        """
        N = len(A)
        memo = [[[0]*N for _ in xrange(N) ] for _ in xrange(N) ]
        
        def dp(i, j, k):
            # from index i to index j, with k same to the left
            if i > j: return 0
            if not memo[i][j][k]:
                m = i
                # here is how to deal with TLE
                # a*a + b*b < (a+b)*(a+b), so as much as we can
                while m+1 <= j and A[m+1] == A[i]:
                    m += 1
                i, k = m, k + m - i
                ans = dp(i+1, j, 0) + (k+1) ** 2 # click on boxes[i] now
                for m in xrange(i+1, j+1):
                    if A[i] == A[m]:
                        # remove all the boxes between i and l first                
                        ans = max(ans, dp(i+1, m-1, 0) + dp(m, j, k+1))
                memo[i][j][k] = ans
            return memo[i][j][k]
        
        return dp(0, N-1, 0)
        

if __name__ == '__main__':
    boxes = [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
    print Solution().removeBoxes(boxes)

# https://discuss.leetcode.com/topic/84687/java-top-down-and-bottom-up-dp-solutions/2
