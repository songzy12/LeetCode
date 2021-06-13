# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def buildTree(self, preorder, inorder):
        if inorder:
            ind = inorder.index(preorder.pop(0)) # size of preorder decrease
            root = TreeNode(inorder[ind])
            root.left = self.buildTree(preorder, inorder[0:ind]) # only inorder
            root.right = self.buildTree(preorder, inorder[ind+1:])
            return root

##    # MLE is due to recursion
##    def __init__(self):
##        self.preorder = []
##        self.inorder = []
##    def buildTree(self, preorder, inorder):
##        """
##        :type preorder: List[int]
##        :type inorder: List[int]
##        :rtype: TreeNode
##        """
##        # MLE
##        if not preorder:
##            return
##        self.preorder = preorder
##        self.inorder = inorder
##        return self.buildTreeHelper(0, len(preorder), 0, len(inorder))
##
##    def buildTreeHelper(self, l_pre, r_pre, l_in, r_in):
##        if l_pre == r_pre:
##            return 
##        root = TreeNode(self.preorder[l_pre])
##        for i in range(l_in, r_in):
##            if self.inorder[i] == self.preorder[l_pre]:
##                l = self.buildTreeHelper(l_pre+1, l_pre+1+(i-l_in), l_in, i)
##                r = self.buildTreeHelper(r_pre-(r_in-i-1), r_pre, i+1, r_in)
##                root.left  = l
##                root.right = r
##                break
##        return root

preorder = [1,2,4,5,3,6]
inorder = [4,2,5,1,3,6]
root = Solution().buildTree(preorder, inorder)
q = [root]
while q:
    t = q.pop(0)
    print t.val,
    if t.left:
        q += t.left,
    if t.right:
        q += t.right,
