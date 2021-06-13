# https://leetcode.com/problems/minimum-cost-to-hire-k-workers/description/


class Solution:

    def mincostToHireWorkers(self, quality, wage, K):
        """
        :type quality: List[int]
        :type wage: List[int]
        :type K: int
        :rtype: float
        """
        rate = [x / y for x, y in zip(wage, quality)]
        # print(rate)
        quality = list(zip(rate, quality))
        quality.sort()

        # print(quality)

        heap = []
        from heapq import heappush, heappop
        cur_sum = 0
        for i in range(K - 1):
            heappush(heap, -quality[i][-1]) 
            cur_sum += quality[i][-1]

        ans = 1 << 32

        for i in range(K - 1, len(quality)):
            cur_rate = quality[i][0]

            cur_sum += quality[i][-1]

            #print(cur_rate, cur_sum * cur_rate)
            ans = min(ans, cur_sum * cur_rate)

            heappush(heap, -quality[i][-1])
            cur_sum += heappop(heap) # NOTE: pop 出最大值
        return ans


quality = [10, 20, 5]
wage = [70, 50, 30]
K = 2
quality = [3, 1, 10, 10, 1]
wage = [4, 8, 2, 2, 7]
K = 3
print(Solution().mincostToHireWorkers(quality, wage, K))
# 对于选出来的 k 个人来说，
# 要满足 k 个人中 rate = wage / quality 最高的那个
# 然后用这个 rate * (sum of qualities)

# 我们可以把 rate 排个序
# 然后枚举最高的 rate 值
