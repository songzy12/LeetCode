# Definition for binary tree with next pointer.
class TreeLinkNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        self.next = None

class Solution(object):
    def connect(self, root):
        """
        :type root: TreeLinkNode
        :rtype: nothing
        """
        head, pre, cur = root, None, None
        while head:
            # next level
            cur, pre, head = head, None, None
            while cur:
                # the same level
                if cur.left:
                    if pre:
                        pre.next = cur.left
                    else:
                        head = cur.left
                    pre = cur.left
                if cur.right:
                    if pre:
                        pre.next = cur.right
                    else:
                        head = cur.right
                    pre = cur.right
                cur = cur.next
                
root = TreeLinkNode(1)
root.left, root.right = TreeLinkNode(2), TreeLinkNode(3)
root.left.left, root.left.right = TreeLinkNode(4), TreeLinkNode(5)
root.right.right = TreeLinkNode(7)
Solution().connect(root)
