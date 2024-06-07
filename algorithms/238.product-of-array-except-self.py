class Solution:
    # @param {integer[]} nums
    # @return {integer[]}
    def productExceptSelf(self, nums):
        if not nums:
            return []
        res = [1]
        temp = 1
        for i in range(len(nums)-1):
            temp *= nums[i]
            res.append(temp)
        temp = 1
        for i in range(len(nums)-1, 0, -1):
            temp *= nums[i]
            res[i-1] *= temp
        return res

nums = []
print(Solution().productExceptSelf(nums))

