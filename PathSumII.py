# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    
    def __init__(self):
        self.ans = []
        
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """
        if not root:
            return []
        self.pathSumHelper(root, 0, sum, [])
        return self.ans
    
    def pathSumHelper(self, root, cur, sum, temp):
        if not root.left and not root.right:
            if sum == cur + root.val:
                self.ans += temp+[root.val],
                return
            else:
                return
        if root.left:
            self.pathSumHelper(root.left, cur+root.val, sum, temp+[root.val])
        if root.right:
            self.pathSumHelper(root.right, cur+root.val, sum, temp+[root.val])
        
        
##root = TreeNode(5)
##root.left, root.right = TreeNode(4), TreeNode(8)
##root.left.left = TreeNode(11)
##root.left.left.left, root.left.left.right = TreeNode(7), TreeNode(2)
##root.right.left, root.right.right = TreeNode(13), TreeNode(4)
##root.right.right.left, root.right.right.right = TreeNode(5), TreeNode(1)
root = TreeNode(-2)
root.right = TreeNode(-3)
sum_ = -5
print Solution().pathSum(root, sum_)
