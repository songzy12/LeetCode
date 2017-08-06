# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def findTarget(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: bool
        """
        if not root:
            return False

        from collections import defaultdict

        m = defaultdict(int)
        q = [root]
        while q:
            node = q.pop(0)
            m[node.val] += 1
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
        for num in m:
            if k - num in m and (k - num != num or m[num] >= 2):
                return True
        return False
