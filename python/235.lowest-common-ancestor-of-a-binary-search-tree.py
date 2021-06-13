# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        if p.val > q.val:
            p, q = q, p
        while not p.val <= root.val <= q.val:
            root = root.left if root.val > q.val else root.right
        return root
    

node = [TreeNode(i) for i in range(10)]
node[6].left, node[6].right = node[2], node[8]
node[2].left, node[2].right = node[0], node[4]
node[4].left, node[4].right = node[3], node[5]
node[8].left, node[8].right = node[7], node[9]

print Solution().lowestCommonAncestor(node[6], node[5], node[0]).val
