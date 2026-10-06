# https://leetcode.com/problems/4sum/description/


class Solution:

    def fourSum(self, nums: list[int], target: int) -> list[list[int]]:
        nums.sort()

        res = set()
        for i in range(len(nums) - 3):
            if nums[i] > target / 4.0:
                break
            for j in range(i + 1, len(nums) - 2):
                if nums[j] > (target - nums[i]) / 3.0:
                    break
                two_sum_res = self.twoSum(nums[j + 1 :], target - nums[i] - nums[j])
                for pair in two_sum_res:
                    res.add(tuple([nums[i], nums[j]] + pair))
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
    nums = [1, 0, -1, 0, -2, 2]
    target = 0
    print(Solution().fourSum(nums, target))
