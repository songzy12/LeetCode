# https://leetcode.com/problems/3sum-closest/


class Solution:
    def threeSumClosest(self, nums: list[int], target: int) -> int:
        nums.sort()

        closed, ans = float("inf"), None
        for i in range(len(nums) - 2):
            two_sum_closed, two_sum_ans = self.twoSumClosest(
                nums[i + 1 :], target - nums[i]
            )

            if two_sum_closed < closed:
                closed = two_sum_closed
                ans = two_sum_ans + nums[i]
        return ans

    def twoSumClosest(self, nums: list[int], target: int) -> tuple[int, int]:
        closed = float("inf")
        ans = None

        left, right = 0, len(nums) - 1
        while left < right:
            s = nums[left] + nums[right]
            if s == target:
                return 0, nums[left] + nums[right]
            elif s < target:
                left += 1
            else:
                right -= 1

            if abs(s - target) < closed:
                closed = abs(s - target)
                ans = s
        return closed, ans
