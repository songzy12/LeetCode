# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # @param root, a tree node
    # @return a list of integers

    def rightSideView(self, root):
        curDepth = 0
        result = []
        l = [root]
        depth = {}
        depth[root] = 1
        while l:
            temp = l.pop()
            if not temp:
                continue
            if depth[temp] > curDepth:
                result += [temp.val]
                curDepth += 1
            depth[temp.right] = depth[temp.left] = depth[temp] + 1
            l = [temp.left, temp.right] + l
        return result
    
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.right = TreeNode(5)
root.right.right = TreeNode(4)

print(Solution().rightSideView(root))
            
