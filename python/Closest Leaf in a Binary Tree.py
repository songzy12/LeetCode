# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def findClosestLeaf(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """        

        sons = {}
        def findSon(node):
            left = [0, None]
            right = [0, None]

            if node.left:
                left = findSon(node.left)
                sons[node.left.val] = left
            if node.right:
                right = findSon(node.right)
                sons[node.right.val] = right
            
            if not left[0] and not right[0]:
                return [1, node.val]
            if not left[0]:
                return [right[0]+1, right[1]]
            if not right[0]:
                return [left[0]+1, left[1]]
            if right[0] < left[0]:
                return [right[0]+1, right[1]]
            return [left[0]+1, left[1]]

        sons[root.val] = findSon(root)

        print(sons)

        fathers = {}
        def findFather(node, l):
            if not node:
                return
            fathers[node.val] = l.copy()
            findFather(node.left, l + [node.val])
            findFather(node.right, l + [node.val])
        findFather(root, [])

        print(fathers[k])
        
        res = sons[k]
        for i, father in enumerate(reversed(fathers[k])):
            if i + 1 + sons[father][0] < res[0]:
                res = [i + 1 + sons[father][0], sons[father][1]]
        return res[-1]
