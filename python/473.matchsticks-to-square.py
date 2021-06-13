class Solution(object):
    def makesquare(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if len(nums) < 4: # corner case
            return False
        if sum(nums) % 4:
            return False
        nums.sort(reverse=True)
        return self.dfs(nums, [0]*4, 0, sum(nums)/4)
    
    def dfs(self, nums, sums, index, target):
        if index == len(nums):
            return sums[0] == sums[1] == sums[2] == target
        for i in range(4):
            if sums[i] + nums[index] > target:
                continue
            sums[i] += nums[index]
            if self.dfs(nums, sums, index + 1, target):
                return True
            sums[i] -= nums[index]
        return False

        
# How can I try out all the possible combinations
# partition problem is in NP, not surprisingly
