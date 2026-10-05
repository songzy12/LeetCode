# https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/description/


class Solution:

    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        """
        Given a 1-indexed array of integers `numbers` that is already sorted in
        non-decreasing order, and an integer `target`, return the indices of the
        two numbers such that they add up to `target`.
        You may assume that each input would have exactly one solution, and you
        may not use the same element twice.
        """
        i, j = 0, len(numbers) - 1
        while i < j:
            if numbers[i] + numbers[j] < target:
                i += 1
            elif numbers[i] + numbers[j] > target:
                j -= 1
            else:
                return i + 1, j + 1


if __name__ == "__main__":
    numbers = [0, 0, 3, 4]
    target = 0
    print(Solution().twoSum(numbers, target))
