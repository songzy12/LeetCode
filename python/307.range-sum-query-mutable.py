class NumArray(object):
    def __init__(self, nums):
        self.nums = nums
        
    def update(self, i, val):
        self.nums[i] = val
        
    def sumRange(self, i, j):
        return sum(self.nums[i:j+1])
    
##    class SegmentTreeNode:
##        def __init__(self, start, end):
##            self.start = start
##            self.end = end
##            self.sum = 0
##            self.left = self.right = None
##        
##    def __init__(self, nums):
##        """
##        initialize your data structure here.
##        :type nums: List[int]
##        """
##        self.root = self.buildTree(nums, 0, len(nums)-1)
##
##    def buildTree(self, nums, start, end):
##        if start > end:
##            return None
##        res = self.SegmentTreeNode(start, end)
##        if start == end:
##            res.sum = nums[start]
##        else:
##            mid = start + (end - start) // 2
##            res.left = self.buildTree(nums, start, mid)
##            res.right = self.buildTree(nums, mid+1, end)
##            res.sum = res.left.sum + res.right.sum
##        return res
##        
##    def update(self, i, val):
##        """
##        :type i: int
##        :type val: int
##        :rtype: int
##        """
##        self.updateTree(self.root, i, val)
##
##    def updateTree(self, root, i, val):
##        if root.start == root.end:
##            root.sum = val
##            return
##        mid = root.start + (root.end - root.start) // 2
##        if i <= mid:
##            self.updateTree(root.left, i, val)
##        else:
##            self.updateTree(root.right, i, val)
##        root.sum = root.left.sum + root.right.sum
##
##    def sumRange(self, i, j):
##        """
##        sum of elements nums[i..j], inclusive.
##        :type i: int
##        :type j: int
##        :rtype: int
##        """
##        return self.sumRangeTree(self.root, i, j)
##
##    def sumRangeTree(self, root, i, j):
##        if (root.start, root.end) == (i, j):
##            return root.sum
##        mid = root.start + (root.end - root.start) // 2
##        if j <= mid:
##            return self.sumRangeTree(root.left, i, j)
##        elif mid + 1 <= i:
##            return self.sumRangeTree(root.right, i, j)
##        else:
##            return self.sumRangeTree(root.left, i, mid) + \
##                   self.sumRangeTree(root.right, mid+1, j)
            
# Your NumArray object will be instantiated and called as such:

nums = [1, 3, 5]
numArray = NumArray(nums)
print numArray.sumRange(0, 2) # 9
numArray.update(1, 2)
print numArray.sumRange(0, 2) # 8
