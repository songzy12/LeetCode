from Tree import *

class Solution:
    # @param root, a tree node
    # @return a list of integers
    def postorderTraversal(self, root):
        l=[]
        if root==None:
            return []
        l.extend(self.postorderTraversal(root.left))
        l.extend(self.postorderTraversal(root.right))
        l.append(root.val)
        return l

root=TreeNode(1)
root.right=TreeNode(2)
root.left=TreeNode(3)
print(Solution().postorderTraversal(root))
