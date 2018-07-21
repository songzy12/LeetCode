# https://leetcode.com/problems/smallest-range/description/
class Solution:

    def smallestRange(self, nums):
        """
        :type nums: List[List[int]]
        :rtype: List[int]
        """
        from heapq import heappop, heappush
        heap = []

        head = nums[0][0]
        tail = nums[0][0]

        ncol = 0
        for nrow, row in enumerate(nums):

            if row[ncol] > tail:
                tail = row[ncol]
            if row[ncol] < head:
                head = row[ncol]
            heappush(heap, (row[ncol], nrow, ncol))

        result = tail - head
        ans = (head, tail)

        while heap:
            val, nrow, ncol = heappop(heap)
            if ncol + 1 < len(nums[nrow]):
                heappush(heap, (nums[nrow][ncol + 1], nrow, ncol + 1))
                head = heap[0][0]
                if nums[nrow][ncol + 1] > tail:
                    tail = nums[nrow][ncol + 1]

                if tail - head < result:
                    result = tail - head
                    ans = (head, tail)
            else:
                break
        return ans


nums = [[4, 10, 15, 24, 26], [0, 9, 12, 20], [5, 18, 22, 30]]
nums = [[1, 2, 3], [1, 2, 3], [1, 2, 3]]
print(Solution().smallestRange(nums))

# 我想大概就是从前往后，记下当前最小位置，
# 记下当前遇到过几个不同队列

# 用一个 heap 来存每一个列表的当前位置值
# 当前 queue 里的最大值就是新加进去的值
