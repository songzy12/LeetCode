# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # @param {TreeNode} root
    # @return {TreeNode}
    def invertTree(self, root):
        if not root:
            return None
        self.invertTree(root.left)
        self.invertTree(root.right)
        root.left, root.right = root.right, root.left
        return root

root = TreeNode(4)
root.left = TreeNode(2)
root.right = TreeNode(7)
root.left.left = TreeNode(1)
root.left.right = TreeNode(3)
root.right.left = TreeNode(6)
root.right.right = TreeNode(9)
root = Solution().invertTree(root)
l = [root]
print(root.val, end = " ")
while l:
    temp = l.pop(0)
    if temp.left:
        print(temp.left.val, end = " ")
        l += [temp.left]
    if temp.right:
        print(temp.right.val, end = " ")
        l += [temp.right]

