class Solution:

    def nthMagicalNumber(self, N, A, B):
        """
        :type N: int
        :type A: int
        :type B: int
        :rtype: int
        """
        import math
        gcd_ = math.gcd(A, B)
        lcm_ = A * B // gcd_
        A //= gcd_
        B //= gcd_

        single_cnt = A + B - 1

        num_round = N // single_cnt
        residule = N % single_cnt

        p = 10**9 + 7

        def compute(residule):
            cur_A = 1
            cur_B = 1
            cnt = 0
            ans = 0
            while cnt != residule:
                if A * cur_A < B * cur_B:
                    ans = A * cur_A
                    cur_A += 1
                else:
                    ans = B * cur_B
                    cur_B += 1
                cnt += 1
            return ans

        # def pow(a, n):
        #     if n == 0:
        #         return 1
        #     temp = pow(a, n // 2)
        #     if n % 2 == 0:
        #         return (temp * temp) % p
        #     else:
        #         return (temp * temp * a) % p

        #print (lcm_, gcd_, num_round, residule, compute(residule))
        ans = lcm_ * num_round + (gcd_ * compute(residule))
        return ans % p

N = 3
A = 6
B = 4
print(Solution().nthMagicalNumber(N, A, B))
