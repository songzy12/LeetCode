# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def countNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        hl = hr = 0
        l = r = root
        while l:
            hl += 1
            l = l.left
        while r:
            hr += 1
            r = r.right
        if hl == hr:
            return (1<<hl) - 1
        return 1 + self.countNodes(root.left) + self.countNodes(root.right)
        

root = TreeNode(0)
root.left = TreeNode(1)
print Solution().countNodes(root)
