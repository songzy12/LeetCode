# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def __init__(self):
        self.ans = 1
        self.m = {}
        
    def depth(self, root):
        if root in self.m:
            return self.m[root]
        if not root:
            return 0
        self.m[root] = max(self.depth(root.left), self.depth(root.right)) + 1
        return self.m[root]
    
    def diameter(self, root):
        if not root:
            return
        if 1 + self.depth(root.left) + self.depth(root.right) > self.ans:
            self.ans = 1 + self.depth(root.left) + self.depth(root.right)
        self.diameter(root.left)
        self.diameter(root.right)
    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.diameter(root)
        return self.ans - 1

# The length of path between two nodes is represented by the number of edges between them.
