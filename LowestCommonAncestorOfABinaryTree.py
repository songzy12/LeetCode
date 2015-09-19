# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        return self.lowestCommonAncestorHelper(root, p, q)[0]
    def lowestCommonAncestorHelper(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        if not root:
            return None, False
        if root == p and root == q:
            return root, True
        # if we have found the answer
        x, found = self.lowestCommonAncestorHelper(root.left, p, q)
        if found:
            return x, True
        y, found = self.lowestCommonAncestorHelper(root.right, p, q)
        if found:
            return y, True
        # if p and q are both in subtree
        if x and y:
            return root, True
        # if root is one of p, q
        if root == q or root == p:
            return root, (True if x or y else False)
        # if at most one in subtree
        return (y, False) if y else (x, False)

##[37,-34,-48,null,-100,-100,48,null,null,null,null,-54,null,-71,-22,null,null,null,8]
##node with value -100
##node with value -100 

node = [TreeNode(i) for i in range(9)]
node[3].left, node[3].right = node[5], node[1]
node[5].left, node[5].right = node[6], node[2]
node[2].left, node[2].right = node[7], node[4]
node[1].left, node[1].right = node[0], node[8]
print Solution().lowestCommonAncestor(node[3], node[6], node[4]).val
##            _3______
##       /              \
##    ___5__          ___1__
##   /      \        /      \
##   6      _2       0       8
##         /  \
##         7   4
