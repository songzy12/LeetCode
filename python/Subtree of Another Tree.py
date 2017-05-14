# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSubtree(self, s, t):
        """
        :type s: TreeNode
        :type t: TreeNode
        :rtype: bool
        """
        def check(t1, t2):
            if not t1 or not t2:
                return not t1 and not t2
            if t1.val != t2.val:
                return False
            return check(t1.left, t2.left) and check(t1.right, t2.right)        
        if not s:
            return not t
        return check(s, t) or self.isSubtree(s.left, t) or self.isSubtree(s.right, t)
            
