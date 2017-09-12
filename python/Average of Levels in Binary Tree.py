# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def averageOfLevels(self, root):
        """
        :type root: TreeNode
        :rtype: List[float]
        """
        level = [root]
        ans = []
        while level:
            next_level = []
            nums = []
            while level:
                temp = level.pop(0)
                if temp.left:
                    next_level.append(temp.left)
                if temp.right:
                    next_level.append(temp.right)
                nums += [temp.val]
            ans.append(sum(nums) * 1. / len(nums))
            level = next_level
        return ans
