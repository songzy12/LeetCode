# Given an integer array, 
# your task is to find all the different possible increasing subsequences of the given array, 
# and the length of an increasing subsequence should be at least 2 .

class Solution(object):
    def findSubsequences(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = set()
        holder = []
        self.findSubsequence(res, holder, 0, nums)
        return list(res)
        
    def findSubsequence(self, res, holder, index, nums):
        if len(holder) >= 2:
            res.add(tuple(holder))
            
        for i in range(index, len(nums)):
            if not holder or holder[-1] <= nums[i]:
                holder += [nums[i]]
                # i+1, rather than index+1
                self.findSubsequence(res, holder, i+1, nums) 
                holder.pop(-1)
        

nums = [1,2,3,4,5,6,7,8,9,10,1,1,1,1,1]
print Solution().findSubsequences(nums)

# no need to use dp, just do backtracking

