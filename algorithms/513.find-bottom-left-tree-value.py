# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def __init__(self):
        self.dp = {}
        
    def findBottomLeftValue(self, root):
        return self.findLeftMostNode(root)
        
    def findLeftMostNode(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if self.findDepth(root) == 1:
            return root.val
        if self.findDepth(root.left) >= self.findDepth(root.right):
            return self.findLeftMostNode(root.left) 
        else:
            return self.findLeftMostNode(root.right) 
        
    def findDepth(self, root):
        if not root:
            return 0
        if root not in self.dp:
            self.dp[root] = max(self.findDepth(root.left), self.findDepth(root.right)) + 1
        return self.dp[root]
