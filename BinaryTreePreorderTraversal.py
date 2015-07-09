from Tree import *
class Solution:
    # @param root, a tree node
    # @return a list of integers
    def preorderTraversal(self, root):
        if root==None:
            return []
        l=[]
        l.append(root.val)
        l.extend(self.preorderTraversal(root.left))
        l.extend(self.preorderTraversal(root.right))
        return l
        # try to do it iteratively when in good mood

root=initTree([1,'#',2,3])
print (Solution().preorderTraversal(root))
