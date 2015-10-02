# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    # Morris Traversal
    def recoverTree(self, root):
        pre, first, second = None, None, None
        temp = None
        while root:
            if root.left:
                temp = root.left
                while temp.right and temp.right != root:
                    temp = temp.right
                if temp.right:
                    if pre and pre.val > root.val:
                        if not first:
                            first, second = pre, root
                        else:
                            second = root
                    pre = root
                    temp.right = None
                    root = root.right
                else:
                    temp.right = root
                    root = root.left
            else:
                if pre and pre.val > root.val:
                    if not first:
                        first, second = pre, root
                    else:
                        second = root
                pre = root
                root = root.right
        first.val, second.val = second.val, first.val

##    def __init__(self):
##        self.first = None
##        self.second = None
##        self.pre = TreeNode(-(1<<31))
##        
##    def recoverTree(self, root):
##        """
##        :type root: TreeNode
##        :rtype: void Do not return anything, modify root in-place instead.
##        """
##        self.traverse(root)
##        self.first.val, self.second.val = self.second.val, self.first.val
##
##    def traverse(self, root):
##        if not root:
##            return
##        self.traverse(root.left)
##        if not self.first and self.pre.val >= root.val:
##            self.first = self.pre
##        if self.first and self.pre.val >= root.val:
##            self.second = root
##        self.pre = root
##        self.traverse(root.right)

root = TreeNode(2)
root.left = TreeNode(3)
root.right = TreeNode(1)
Solution().recoverTree(root)
print root.left.val, root.val, root.right.val
