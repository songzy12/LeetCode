# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def sumNumbers(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        return sum(map(lambda i: int(i), self.sumNumbersHelper(root)))
    def sumNumbersHelper(self, root):
        if not root.left and not root.right:
            return [str(root.val)]
        ans = []
        if root.left:
            ans += [str(root.val)+i for i in self.sumNumbersHelper(root.left)]
        if root.right:
            ans += [str(root.val)+i for i in self.sumNumbersHelper(root.right)]
        return ans
               

node = [TreeNode(i) for i in range(1,6)]
node[0].left, node[0].right = node[1], node[2]
node[1].left, node[1].right = node[3], node[4]
print Solution().sumNumbers(node[0])
