from Tree import *

class Solution:
    # @param root, a tree node
    # @param sum, an integer
    # @return a boolean
    def hasPathSum(self, root, sum):
        if root==None:
            return False
        if root.left==None and root.right==None:
            return root.val==sum
        if root.left==None:
            return self.hasPathSum(root.right, sum-root.val)
        if root.right==None:
            return self.hasPathSum(root.left, sum-root.val)
        return self.hasPathSum(root.left,sum-root.val) or \
               self.hasPathSum(root.right, sum-root.val)
        
sum=22
root=TreeNode(5)
root.left=TreeNode(4)
root.left.left=TreeNode(11)
root.left.left.right=TreeNode(2)
print(Solution().hasPathSum(root,sum))
