import time
class Solution(object):
    def nthSuperUglyNumber(self, n, primes):
        """
        :type n: int
        :type primes: List[int]
        :rtype: int
        """
        import heapq
        q, uglyNums = [], [1]
        k = len(primes)
        for i in range(k): heapq.heappush(q, (primes[i], 0, primes[i]))
        while len(uglyNums) < n:
            x, i, p = q[0]
            uglyNums += [x]
            while q and q[0][0] == x:
                x, i, p = heapq.heappop(q)
                heapq.heappush(q, (p * uglyNums[i+1], i+1, p))
        return uglyNums[-1]

##        # indices[i] is the index of ugly number which will
##        # generate the next number when multiplying prime[i]
##        indices = [0 for i in range(len(primes))]
##        ret = [(1<<31) for i in range(n)]
##        ret[0] = 1
##        for i in range(1, n):
##            for j in range(len(primes)):
##                ret[i] = min(ret[i], ret[indices[j]]*primes[j])
##            for j in range(len(primes)):
##                if ret[i] == ret[indices[j]]*primes[j]:
##                    indices[j] += 1
##                    # there should be no break
##        return ret[-1]

start = time.time()
n = 200000
primes = [2,3,5,13,19,29,31,41,43,53,59,73,83,89,97,103,107,109,127,137,139,149,163,173,179,193,197,199,211,223,227,229,239,241,251,257,263,269,271,281,317,331,337,347,353,359,367,373,379,389,397,409,419,421,433,449,457,461,463,479,487,509,521,523,541,547,563,569,577,593,599,601,613,619,631,641,659,673,683,701,709,719,733,739,743,757,761,769,773,809,811,829,857,859,881,919,947,953,967,971]
print Solution().nthSuperUglyNumber(n, primes)
print time.time() - start
