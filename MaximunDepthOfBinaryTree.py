from Tree import *
class Solution:
    # @param root, a tree node
    # @return an integer
    def maxDepth(self, root):
        if root == None:
            return 0
        if root.left==None or root.right==None:
            return self.maxDepth(root.left)+self.maxDepth(root.right)+1
        return max(self.maxDepth(root.right),self.maxDepth(root.left))+1

print (Solution().maxDepth(initTree([1,2,3,'#','#','#',4])))

