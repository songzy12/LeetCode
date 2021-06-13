# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def buildTree(self, inorder, postorder):
        """
        :type inorder: List[int]
        :type postorder: List[int]
        :rtype: TreeNode
        """
        if inorder:
            root = TreeNode(postorder[-1])
            i = inorder.index(postorder.pop())
            root.right = self.buildTree(inorder[i+1:], postorder)
            root.left = self.buildTree(inorder[:i], postorder)
            return root
        
inorder = [1,2,3,4,5,6]
postorder = [1,3,2,6,5,4]
root = Solution().buildTree(inorder, postorder)
q = [root]
while q:
    t = q.pop(0)
    print t.val,
    if t.left:
        q += t.left,
    if t.right:
        q += t.right,
