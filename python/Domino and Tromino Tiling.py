class Solution:
    def numTilings(self, N):
        """
        :type N: int
        :rtype: int
        """

        p = 10**9+7
        a = {}
        b = {}

        def get_a(N):
            if N in a:
                return a[N]
            if N == 0:
                return 1
            if N == 1:
                return 1            
            a[N] = get_a(N-1) + get_a(N-2) +  2*get_b(N-1)
            a[N] %= p
            return a[N]
        def get_b(N):
            if N in b:
                return b[N]
            if N == 0:
                return 1
            if N == 1:
                return 0
            if N == 2:
                return 1
            b[N] = get_b(N-1) + get_a(N-2)
            b[N] %= p
            return b[N]
        return get_a(N)

N = 30
print(Solution().numTilings(N))
            
