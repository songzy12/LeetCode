# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def flatten(self, root):
        while root:
            if root.left:
                ptr = root.left
                while ptr.right:
                    ptr = ptr.right
                ptr.right = root.right
                root.right = root.left
                root.left = None
            root = root.right


##    # TLE    
##    def flatten(self, root):
##        if not root:
##            return
##        right_stack  = []
##        while root:
##            if root.right:
##                right_stack += root.right,
##            if root.left:
##                root.right = root.left
##                root = root.left
##            elif right_stack:
##                root.right = right_stack.pop()
##                root = root.right
##            else:
##                return                

##    # TLE        
##    def flattenHelper(self, root):
##        if not root:
##            return []
##        return [root] + self.flattenHelper(root.left) +\
##               self.flattenHelper(root.right)

##    # TLE    
##    def flattenHelper(self, root):
##        if not root.left and not root.right:
##            return root
##        if not root.right:
##            root.right = root.left
##            return self.flattenHelper(root.left)
##        if not root.left:
##            return self.flattenHelper(root.right)
##        l, r = self.flattenHelper(root.left), self.flattenHelper(root.right)
##        l.right = root.right
##        root.right = root.left
##        return r
        
node = [TreeNode(i) for i in range(1, 7)]
node[0].left, node[0].right = node[1], node[4]
node[1].left, node[1].right = node[2], node[3]
node[4].right = node[5]
Solution().flatten(node[0])
head = node[0]
while head:
    print head.val,
    head = head.right
