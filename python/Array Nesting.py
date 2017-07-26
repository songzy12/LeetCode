class Solution(object):
    def arrayNesting(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        visited = [False]*len(nums)

        def get_cycle_size(i):
            size = 0
            while not visited[i]:
                size += 1
                visited[i] = True
                i = nums[i]
            return size
        ans = 0
        for i in range(len(nums)):
            if visited[i]:
                continue
            temp = get_cycle_size(i)
            if temp > ans:
                ans = temp
        return ans
