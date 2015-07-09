class Solution:
    # @param {integer[]} nums
    # @return {string[]}
    def summaryRanges(self, nums):
        if not nums:
            return []
        res = []
        temp = 0
        i = 0
        while i+1 < len(nums):
            if nums[i+1]-nums[i] != 1:
                if temp != i:
                    res += [str(nums[temp]) + "->"+str(nums[i])]
                else:
                    res += [str(nums[temp])]
                temp = i+1
            i += 1
        if temp != i:
            res += [str(nums[temp]) + "->"+str(nums[i])]
        else:
            res += [str(nums[temp])]
        return res

nums = [0,3,4,5,7,9,10]
print(Solution().summaryRanges(nums))
            
