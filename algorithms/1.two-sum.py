# https://leetcode.com/problems/two-sum/description/
#
# Test cases:
# [3, 2, 4], 6 -> [1, 2]
# [3, 3], 6 -> [0, 1]


class Solution:

    def twoSum(self, nums: list[int], target: int) -> list[int]:
        """
        Given an array of integers `nums` and an integer `target`, return the
        indices of the two numbers such that they add up to `target`.
        You may assume that each input would have exactly one solution, and you
        may not use the same element twice.
        """
        d = {}
        for i, num in enumerate(nums):
            if target - num in d:
                return [d[target - num], i]
            else:
                d[num] = i


if __name__ == "__main__":
    nums = [3, 2, 4]
    target = 6
    print(Solution().twoSum(nums, target))

    nums = [3, 3]
    target = 6
    print(Solution().twoSum(nums, target))
