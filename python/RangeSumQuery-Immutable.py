class NumArray(object):
    def __init__(self, nums):
        """
        initialize your data structure here.
        :type nums: List[int]
        """
        self.partial = [0]
        for i in nums:
            self.partial += self.partial[-1] + i,
        
    def sumRange(self, i, j):
        """
        sum of elements nums[i..j], inclusive.
        :type i: int
        :type j: int
        :rtype: int
        """
        return self.partial[j+1] - self.partial[i]


# Your NumArray object will be instantiated and called as such:
nums = [1,2,3,4]
numArray = NumArray(nums)
print numArray.sumRange(0, 1)
print numArray.sumRange(1, 3)
