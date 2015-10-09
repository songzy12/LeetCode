class Solution(object):
    def nthUglyNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        ugly = [1]
        ind2 = ind3 = ind5 = 0
        fac2 = fac3 = fac5 = 1
        for i in range(1,n):
            nextUgly = min(2*fac2, 3*fac3, 5*fac5)
            ugly += nextUgly,
            if nextUgly == 2*fac2:
                ind2 += 1
                fac2 = ugly[ind2]
            if nextUgly == 3*fac3:
            # not elif, since 3*2 == 2*3
                ind3 += 1
                fac3 = ugly[ind3]
            if nextUgly == 5*fac5:
                ind5 += 1
                fac5 = ugly[ind5]
        return ugly[-1]

for i in range(1,12):
    print Solution().nthUglyNumber(i)
