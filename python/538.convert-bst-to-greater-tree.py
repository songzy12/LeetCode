# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def down(self, root, res):
        if root.right:
            res = self.down(root.right, res)
        root.val += res
        res = root.val
        if root.left:
            res = self.down(root.left, root.val)
        return res
        
        
    def convertBST(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if not root:
            return root
        self.down(root, 0)
        return root
        
        
