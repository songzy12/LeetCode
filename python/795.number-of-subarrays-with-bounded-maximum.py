class Solution:
    def numSubarrayBoundedMax(self, A, L, R):
        """
        :type A: List[int]
        :type L: int
        :type R: int
        :rtype: int
        """
        ans = 0
        cur = []
        length = 0

        def deal(cur, length):
            # print(length, cur)
            
            res = length * (length + 1) // 2
            for x in cur:
                res -= x * (x+1) // 2
            return res
            
        l = -1
        for i, num in enumerate(A):
            if num > R:
                r = i
                if length > 0:
                    cur.append(length)
                ans += deal(cur, r - l - 1)
                cur = []
                length = 0
                l = i
            else:
                if num >= L:
                    if length > 0:
                        cur.append(length)
                    length = 0
                else:
                    length += 1

        cur.append(length)
        ans += deal(cur, len(A) - l - 1)
        return ans
        

A = [16,69,88,85,79,87,37,33,39,34]
L = 55
R = 57
print(Solution().numSubarrayBoundedMax(A, L, R))
