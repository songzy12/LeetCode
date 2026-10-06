# https://leetcode.com/problems/two-sum-iv-input-is-a-bst/description/


from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        left = root
        right = root
        return self.findTargetHelper(left, right, k)

    def findTargetHelper(
        self, left: Optional[TreeNode], right: Optional[TreeNode], k: int
    ) -> bool:
        if not left or not right:
            return False

        if left.val + right.val == k:
            if left != right:
                return True
            return self.findTargetHelper(left.left, right.right, k)

        if left.val + right.val < k:
            if left == right:
                return self.findTargetHelper(left, right.right, k)
            else:
                return self.findTargetHelper(
                    left.right, right, k
                ) or self.findTargetHelper(left, right.right, k)

        if left.val + right.val > k:
            if left == right:
                return self.findTargetHelper(left.left, right, k)
            else:
                return self.findTargetHelper(
                    left.left, right, k
                ) or self.findTargetHelper(left, right.left, k)

        # Actually we will not reach here because all cases are covered above.
        return False
