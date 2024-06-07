# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def pruneTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        def isValid(root):
            valid = False
            if root.left:
                if not isValid(root.left):
                    root.left = None
                else:
                    valid = True
                    
            if root.right:
                if not isValid(root.right):
                    root.right = None
                else:
                    valid = True
            if root.val:
                valid = True
            return valid
        
        valid = isValid(root)
        if valid:
            return root
        else:
            return None
        
                
                
                
            
