# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        return self.kthSmallestHelper(root)[k-1]
        
    def kthSmallestHelper(self, root):
        if not root:
            return []
        return self.kthSmallestHelper(root.left) + [root.val] + \
               self.kthSmallestHelper(root.right)


node = [TreeNode(i) for i in range(5)]
node[2].left = node[1]
node[2].right = node[3]
node[1].left = node[0]
node[3].right = node[4]
print Solution().kthSmallest(node[2],2)
