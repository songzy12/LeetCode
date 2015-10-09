class Solution:
    # @param {integer} n
    # @return {integer}
    def countPrimes(self, n):
        numbers = [0, 0] + [1 for i in range(2, n)]
        for i in range(2,int(n**0.5)):
            if numbers[i]==0:
                continue
            t = 2
            while t * i < n:
                numbers[t*i] = 0
                t += 1
        count = 0
        for i in range(2, n):
            if numbers[i] == 1:
                count += 1
        return count

print(Solution().countPrimes(10000000))
