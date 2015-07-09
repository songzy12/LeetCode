class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # @param {TreeNode} root
    # @return {integer[][]}
    def levelOrder(self, root):
        # always remember corner case
        if not root:
            return []
        pre = 1
        cur = 0
        l = [root]
        result = []
        while pre:
            t = []
            for i in range(pre):
                temp = l.pop()
                t.append(temp.val)
                if temp.left:
                    l = [temp.left] + l
                    cur += 1
                if temp.right:
                    l = [temp.right] + l
                    cur += 1
            result.append(t)
            pre = cur
            cur = 0
        return result

root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)
print(Solution().levelOrder(root))
print(Solution().levelOrder(None))

                
