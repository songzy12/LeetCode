class TreeNode:
 def __init__(self, x):
     self.val = x
     self.left = None
     self.right = None

class Solution:
    # @param num, a list of integers
    # @return a tree node
    def sortedArrayToBST(self, num):
        if len(num)==0:
            return None
        if len(num)==1:
            return TreeNode(num[0])
        index=len(num)//2
        root=TreeNode(num[index])
        root.left=self.sortedArrayToBST(num[:index])
        root.right=self.sortedArrayToBST(num[index+1:])
        return root
