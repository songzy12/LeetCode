# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):

    def __init__(self):
        self.currVal = None
        self.currCount = 0
        self.maxCount = 0
        self.modeCount = 0
        self.modes = None
        
    def findMode(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        self.inorder(root)
        self.modes = [None]*self.modeCount
        self.modeCount = 0
        self.currCount = 0
        self.inorder(root)
        return self.modes
    
    def handleValue(self, val):
        # since in-order and BST, 
        # so same numbers are handled consecutively
        if val != self.currVal:
            self.currVal = val
            self.currCount = 0
        self.currCount += 1
        if self.currCount > self.maxCount:
            self.maxCount = self.currCount
            self.modeCount = 1
        elif self.currCount == self.maxCount:
            if self.modes:
                self.modes[self.modeCount] = self.currVal
            self.modeCount += 1
            
    def inorder(self, root):
        if not root:
            return
        self.inorder(root.left)
        self.handleValue(root.val)
        self.inorder(root.right)
