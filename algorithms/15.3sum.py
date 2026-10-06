# https://leetcode.com/problems/3sum/description/


class Solution:

    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        res = set()
        for i in range(len(nums) - 2):
            two_sum_res = self.twoSum(nums[i + 1 :], -nums[i])
            for pair in two_sum_res:
                res.add(tuple([nums[i]] + pair))
        return [list(t) for t in res]

    def twoSum(self, nums: list[int], target: int) -> list[list[int]]:
        res = []
        left, right = 0, len(nums) - 1
        while left < right:
            s = nums[left] + nums[right]
            if s == target:
                res.append([nums[left], nums[right]])
                left += 1
                right -= 1
            elif s < target:
                left += 1
            else:
                right -= 1
        return res


if __name__ == "__main__":
    nums = [-1, 0, 1, 2, -1, -4]
    print(Solution().threeSum(nums))
