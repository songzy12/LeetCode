# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def largestValues(self, root):
        return self.findValueMostElement(root)
        
    def findValueMostElement(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []
        rows = self.getRows(root)
        return [max(x) for x in rows]
        
    def getRows(self, root):
        ans = []
        temp = [root]
        while temp:
            cur = temp[:]
            temp = []
            for x in cur:
                if x.left:
                    temp += x.left,
                if x.right:
                    temp += x.right,
            ans += [x.val for x in cur],
        return ans
