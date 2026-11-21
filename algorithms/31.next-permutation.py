# https://leetcode.com/problems/next-permutation/description/


class Solution:

    def nextPermutation(self, nums):
        """Three steps:
        1. Find the longest increasing sequence from the end, as well as the element A just before it.
        2. Find the element B in the longest increasing sequence that is just larger than A, then swap A and B, so that now A is part of the increasing sequence, while B is just before the increasing sequence.
        3. Reverse the increasing sequence from the end to be decreasing from the end.
        """
        if not nums or len(nums) == 1:
            return

        index_A = self.findIndexA(nums)
        if index_A == -1:
            nums[::] = nums[::-1]
            return

        index_B = self.findIndexB(nums, index_A)
        # print("index_A, index_B:", index_A, index_B)
        # print("increasing sequence from the end:", nums[index_A+1:])
        # print("element A:", nums[index_A])
        # print("element B:", nums[index_B])
        nums[index_A], nums[index_B] = nums[index_B], nums[index_A]
        # print("after swap:", nums)

        nums[index_A+1:] = nums[index_A+1:][::-1]
        # print("after reverse:", nums)

    def findIndexA(self, nums):
        for i in range(len(nums) - 2, -1, -1):
            if nums[i] < nums[i+1]:
                return i
        return -1

    def findIndexB(self, nums, index_A):
        # We know that index_B must be >= index_A + 1
        # since nums[index_A + 1] > nums[index_A]
        # since that is the definition of index_A
        for i in range(len(nums) - 1, -1, -1):
            if nums[i] > nums[index_A]:
                return i


if __name__ == '__main__':
    nums = [1, 2, 3, 4, 5]
    count = 0

    s = Solution()
    while True:
        print(nums)
        count += 1

        s.nextPermutation(nums)
        if nums == [1, 2, 3, 4, 5]:
            break
    print("Total permutations:", count)
