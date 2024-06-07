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

# 将每一个列表的最小的元素都存进一个 heap
# 记录 head 和 tail, 分别是 heap 中当前最小值和当前最大值
# 每次 pop 一个最小值出来，并将同个列表的下个数字 push 进 heap
# head 就是当前 heap 顶端的值
# tail 就是刚刚 push 进去的值和上个 tail 之中较大的那个
# 然后计算 tail - head
