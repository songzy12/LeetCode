# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def checkEqualTree(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return False
        m = {}

        def get_sum(node):
            if not node:
                return 0
            temp = node.val + get_sum(node.left) + get_sum(node.right)
            m[temp] = m.get(temp, 0) + 1
            return temp
        
        tot = get_sum(root)
        if tot:
            return tot % 2 == 0 and (tot / 2) in m
        return m[0] > 1

    
        
        
