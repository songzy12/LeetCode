class Solution:
    # @param {integer[]} nums
    # @return {boolean}
    def containsDuplicate(self, nums):
        return len(nums)>len(set(nums))
##        m = {}
##        for i in nums:
##            if i not in m:
##                m[i] = 1
##            else:
##                return True
##        return False
print(Solution().containsDuplicate([1,1,2]))
