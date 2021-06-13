# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def str2tree(self, s):
        """
        :type s: str
        :rtype: TreeNode
        """
        if not s:
            return None
        head = ''
        i = 0
        while i < len(s):
            if s[i] == '(':
                break
            head += s[i]
            i += 1

        def get_group(i):
            i += 1
            res = ''
            balance = 1
            while i < len(s):
                if s[i] == ')':
                    balance -= 1
                elif s[i] == '(':
                    balance += 1
                if balance == 0:
                    break                
                res += s[i]
                i += 1
            return res, i + 1
        
        left, i = get_group(i)
        right, i = get_group(i)
            
        root = TreeNode(int(head))
        root.left = self.str2tree(left)
        root.right = self.str2tree(right)
        return root
