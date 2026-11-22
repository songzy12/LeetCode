# https://leetcode.com/problems/permutations-ii/description/

class Solution:
    def permuteUnique(self, nums):
        if len(nums) <= 1:
            return [nums]

        ans = []
        visited = set()
        for i in range(len(nums)):
            if nums[i] in visited:
                continue
            visited.add(nums[i])
            pivot = nums[i]
            left = nums[:i] + nums[i+1:]
            for perm in self.permuteUnique(left):
                ans.append([pivot] + perm)
        return ans


if __name__ == '__main__':
    nums = [1, 1, 2, 3]
    for perm in Solution().permuteUnique(nums):
        print(perm)
