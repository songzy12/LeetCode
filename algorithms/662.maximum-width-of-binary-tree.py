# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def widthOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        ans = 1
        cur_layer = [root]
        while cur_layer:
            next_layer = []
            for node in cur_layer:
                if node:
                    next_layer += [node.left, node.right]
                else:
                    next_layer += [None, None]
            i = 0
            j = len(next_layer) - 1
            while i <= j and not next_layer[i]:
                i += 1
            while j >= i and not next_layer[j]:
                j -= 1
            cur_layer = next_layer[i:j+1]

            if len(cur_layer) > ans:
                ans = len(cur_layer)
        return ans
