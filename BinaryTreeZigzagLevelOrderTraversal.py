# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # @param {TreeNode} root
    # @return {integer[][]}
    def zigzagLevelOrder(self, root):
        result = []
        self.dfs(root, result, 0)
        return result

    def dfs(self, node, result, level):
        if not node:
            return
        if len(result)<=level:
            result += [[]]
        if level % 2 == 0:
            result[level] += [node.val]
        else:
            result[level] = [node.val] + result[level]
        self.dfs(node.left, result, level+1)
        self.dfs(node.right, result, level+1)
        
##    def zigzagLevelOrder(self, root):
##        if not root:
##            return []
##        right = []
##        left = [root]
##        result = []
##        while left or right:
##            temp_left = []
##            while left:
##                temp = left.pop(0)
##                if temp.left:
##                    right += [temp.left]
##                if temp.right:
##                    right += [temp.right]
##                temp_left += [temp.val]
##            if temp_left:
##                result = result + [temp_left]
##
##            temp_right = []
##            while right:
##                temp = right.pop()
##                if temp.right:
##                    left = [temp.right] + left
##                if temp.left:
##                    left = [temp.left] + left
##                temp_right += [temp.val]
##            if temp_right:
##                result = result + [temp_right]
##        return result

root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)
print(Solution().zigzagLevelOrder(root))
