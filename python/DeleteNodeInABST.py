# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def deleteNode(self, root, key):
        """
        :type root: TreeNode
        :type key: int
        :rtype: TreeNode
        """
        father = None
        right = None
        dummy = TreeNode(-1<<32)
        dummy.right = root
        temp = dummy
        while temp and temp.val != key:
            father = temp
            if temp.val > key:
                temp = temp.left
                right = False
            else:
                temp = temp.right
                right = True
        if not temp: # not found
            return dummy.right
        if not temp.left:
            if right:
                father.right = temp.right
            else:
                father.left = temp.right
            return dummy.right
        if not temp.left.right:
            temp.left.right = temp.right
            if right:
                father.right = temp.left
            else:
                father.left = temp.left
            return dummy.right
        temp2 = temp.left.right
        father2 = temp.left
        while temp2.right:
            father2 = temp2
            temp2 = temp2.right
        father2.right = temp2.left
        temp2.left = temp.left
        temp2.right = temp.right
        if right:
            father.right = temp2
        else:
            father.left = temp2
        return dummy.right
