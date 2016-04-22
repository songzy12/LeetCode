# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def __init__(self):
        self.f = {} # contain
        self.g = {} # not contain

    def get_f(self, node):
        if not node:
            return 0
        if node in self.f:
            return self.f[node]
        self.f[node] = node.val + self.get_g(node.left) + self.get_g(node.right)
        return self.f[node]

    def get_g(self, node):
        if not node:
            return 0
        if node in self.g:
            return self.g[node]
        self.g[node] = max(self.get_f(node.left), self.get_g(node.left)) + \
                  max(self.get_f(node.right), self.get_g(node.right))
        return self.g[node]
    
    def rob(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        return max(self.get_f(root), self.get_g(root))
