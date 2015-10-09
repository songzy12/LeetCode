from Tree import *
class Solution:
    # @param root, a tree node
    # @return a boolean
    def isSymmetric(self, root):
        if root==None:
            return True
        else:
            return self.auxIsSymmetric(root.left,root.right)
    def auxIsSymmetric(self, left, right):
        if left==None or right==None:
            return left==None and right==None
        return left.val==right.val and \
               self.auxIsSymmetric(left.left,right.right) and \
               self.auxIsSymmetric(left.right,right.left)
    
root=TreeNode(1)
root.left=TreeNode(2)
root.right=TreeNode(2)
root.left.right=TreeNode(3)
root.right.right=TreeNode(3)
print(Solution().isSymmetric(root))
