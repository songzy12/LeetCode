# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        if not root:
            return []
        if not root.left and not root.right:
            return [str(root.val)]
        if not root.right:
            return [str(root.val)+'->' + path for path in self.binaryTreePaths(root.left)]
        if not root.left:
            return [str(root.val)+'->' + path for path in self.binaryTreePaths(root.right)]
        return [str(root.val) +'->' + path for path in self.binaryTreePaths(root.left)+self.binaryTreePaths(root.right)]

nodes = [TreeNode(i) for i in range(0,6)]
nodes[1].left = nodes[2]
nodes[1].right = nodes[3]
nodes[2].right = nodes[5]
print Solution().binaryTreePaths(None)

