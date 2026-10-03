# https://leetcode.com/problems/two-sum/description/
#
# Test cases:
# [3, 2, 4], 6 -> [1, 2]
# [3, 3], 6 -> [0, 1]


class Solution:

    def twoSum(self, nums: list[int], target: int) -> list[int]:
        d = {}
        for i, num in enumerate(nums):
            if target - num in d:
                return [d[target - num], i]
            else:
                d[num] = i


if __name__ == "__main__":
    num = [3, 2, 4]
    target = 6
    print(Solution().twoSum(num, target))

    num = [3, 3]
    target = 6
    print(Solution().twoSum(num, target))
