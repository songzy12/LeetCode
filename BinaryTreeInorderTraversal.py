from Tree import *

class Solution:
    # @param root, a tree node
    # @return a list of integers
    def inorderTraversal(self, root):
        if root==None:
            return []
        l=[]
        l.extend(self.inorderTraversal(root.left))
        l.append(root.val)
        l.extend(self.inorderTraversal(root.right))
        return l
    
root=TreeNode(1)
root.left=TreeNode(2)
print(Solution().inorderTraversal(root))
