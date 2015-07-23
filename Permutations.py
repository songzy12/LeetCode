class Solution:
    # @param {integer[]} nums
    # @return {integer[][]}
    def permute(self, nums):
        if len(nums) <= 1:
            return [nums]
        ans = [nums]
        temp = self.next_permute(nums)
        while temp != nums:
            # print(temp)
            ans += [temp]
            temp = self.next_permute(temp)
        return ans
    
    def next_permute(self, nums):
        i = 0
        for i in range(len(nums)-1, 0, -1):
            if nums[i-1] < nums[i]:
                # len(nums) > 1 
                break
        else: # if not break
            return sorted(nums)
        temp = nums[i:]
        temp.sort()
        mid = 0
        for t in range(len(temp)):
            if temp[t] > nums[i-1]:
                mid = temp[t]
                break
        return nums[:i-1] + [mid] + temp[:t] + [nums[i-1]] + temp[t+1:]
                
nums = [1]
print(len(Solution().permute(nums)))
