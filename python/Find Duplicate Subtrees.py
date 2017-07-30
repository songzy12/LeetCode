# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def __init__(self):
        self.ans = []
        self.appeared = {}
        self.visited = {}

    def traverse(self, node):
        if not node:
            return [None]
        left = self.traverse(node.left)
        right = self.traverse(node.right)
        cur = [node.val] + left + right # left + cur + right , is not unique
        print cur
        if tuple(cur) in self.appeared and tuple(cur) not in self.visited:
            self.ans += [node]
            self.visited[tuple(cur)] = True
        self.appeared[tuple(cur)] = True
        return cur
        
    def findDuplicateSubtrees(self, root):
        """
        :type root: TreeNode
        :rtype: List[TreeNode]
        """   
        self.traverse(root)
        return self.ans
        
        
# [0,0,0,0,null,null,0,null,null,null,0]
# [[0]]
