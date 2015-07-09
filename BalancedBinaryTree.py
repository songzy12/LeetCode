# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # @param root, a tree node
    # @return a boolean

    def isBalanced(self, root):
        return self.height(root)!=-1
    def height(self, root):
        # depth first search
        if root==None:
            return 0
        lheight = self.height(root.left)
        rheight = self.height(root.right)
        if lheight == -1 or rheight == -1:
            return -1
        if rheight-lheight>1 or rheight-lheight<-1:
            return -1
        return max(lheight, rheight)+1


##    def isBalanced(self, root):
##        # the depth of two subtrees of every node differ by more than 1
##        return True if root==None else (
##            self.isBalanced(root.left) and
##            self.isBalanced(root.right) and
##            -1 <= self.depth(root.left)-self.depth(root.right) <= 1)
##
##    def depth(self, root):
##        return 0 if root==None else (
##            max(self.depth(root.left), self.depth(root.right))+1)

root=TreeNode(0)
node1=TreeNode(1)
node2=TreeNode(2)
root.left=node1
root.right=node2
node3=TreeNode(3)
node1.left=node3
#node4=TreeNode(4)
#node3.left=node4

print(Solution().isBalanced(root))
