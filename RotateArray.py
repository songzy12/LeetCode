class Solution:
    # @param nums, a list of integer
    # @param k, num of steps
    # @return nothing, please modify the nums list in-place.
    def rotate(self, nums, k):
        # notice right rotate or left rotate
        nums[::]=nums[len(nums)-k::]+nums[:len(nums)-k:]

n=[1,2]
k=3
Solution().rotate(n,k)
print(n)
