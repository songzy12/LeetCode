# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def findTilt(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        s = {}
        def get_s(node):
            if not node:
                return 0
            if node in s:
                return s[node]
            s[node] = node.val + get_s(node.left) + get_s(node.right)
            return s[node]
        def get_t(node):
            if not node:
                return 0
            return abs(get_s(node.left) - get_s(node.right))
        ans = 0
        q = [root]
        while q:
            node = q.pop(0)
            if node:
                q.append(node.left)
                q.append(node.right)
                ans += get_t(node)
        return ans
            
            
            
            
