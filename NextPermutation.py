class Solution:
    # @param {integer[]} nums
    # @return {void} Do not return anything, modify nums in-place instead.
    def nextPermutation(self, nums):
        if not nums or len(nums)==1:
            return
        for i in range(len(nums)-1, -1, -1):
            if i == 0 or nums[i-1] < nums[i]:
                break
        if i == 0:
            nums[::] = nums[::-1]
            return 
        temp = nums[i-1]
        for j in range(len(nums)-1,i-1,-1):
            if nums[j] > temp:
                nums[i-1] = nums.pop(j)
                break
        nums[i:] = nums[len(nums)-1:j-1:-1]+[temp]+nums[j-1:i-1:-1]
        return

'''
nums = [5,4,2,3,1]
Solution().nextPermutation(nums)
print(nums)
'''

nums = [1,2,3,4,5]
count = 1
while nums != [5,4,3,2,1]:
    Solution().nextPermutation(nums)
    count += 1
    print(nums)
print(count)

