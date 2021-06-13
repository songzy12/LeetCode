# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        return self.isValidBSTHelper(root, None, None)
    def isValidBSTHelper(self, root, l, r):
        if not root:
            return True
        if l!=None and root.val <= l: # 0!=None
            return False
        if r!=None and root.val >= r:
            return False
        return self.isValidBSTHelper(root.left, l, root.val) and \
               self.isValidBSTHelper(root.right, root.val, r)

node = [TreeNode(i) for i in range(1, 7)]
node[2].left, node[2].right = node[1], node[4]
node[1].left, node[1].right = node[0], node[3]
node[4].right = node[5]
print Solution().isValidBST(node[2])
