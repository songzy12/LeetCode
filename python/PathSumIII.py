# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def __init__(self):
        self.count = 0
        self.presum = {}
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: int
        """
        self.presum[0] = 1
        self.helper(root, sum, 0)
        return self.count
    def helper(self, root, sum, pathsum):
        if not root:
            return 
        pathsum += root.val
        self.count += self.presum.get(pathsum - sum, 0)
        self.presum[pathsum] = self.presum.get(pathsum, 0) + 1
        self.helper(root.left, sum, pathsum)
        self.helper(root.right, sum, pathsum)
        self.presum[pathsum] = self.presum.get(pathsum, 0) - 1
        

# if (pathsum-target) is in the preSum
# then we know that at some node of path we have a (pathsum-target) preSum
# hence we have a path of target
