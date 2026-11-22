# https://leetcode.com/problems/permutations/description/

class Solution:
    def permute(self, nums):
        if len(nums) <= 1:
            return [nums]

        ans = []
        for i in range(len(nums)):
            pivot = nums[i]
            left = nums[:i] + nums[i+1:]
            for perm in self.permute(left):
                ans.append([pivot] + perm)
        return ans


if __name__ == '__main__':
    nums = [1, 2, 3]
    for perm in Solution().permute(nums):
        print(perm)
