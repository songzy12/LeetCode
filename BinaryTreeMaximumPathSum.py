# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # @param {TreeNode} root
    # @return {integer}
    def maxPathSum(self, root):
        self.maxSum = -2**31
        self.maxDown(root)
        return self.maxSum

    def maxDown(self, root):
        if root == None:
            return 0
        left = max(0,self.maxDown(root.left))
        right = max(0,self.maxDown(root.right))
        self.maxSum = max(self.maxSum, root.val + left + right)
        return max(left, right) + root.val
        

root = TreeNode(-3)
print(Solution().maxPathSum(root))
