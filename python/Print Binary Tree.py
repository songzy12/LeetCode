# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def printTree(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[str]]
        """
        if not root:
            return []
        
        cur_layer = []
        next_layer = [root]
        flat = []
        flag = True
        while flag:
            flag = False
            flat.append(list(next_layer))
            cur_layer, next_layer = next_layer, []
            while cur_layer:
                node = cur_layer.pop(0)
                if node:
                    flag = True
                    next_layer += [node.left, node.right]
                else:
                    next_layer += [None, None]
        flat.pop(-1)
        n = len(flat)

        ans = []
        for t, layer in enumerate(flat):
            num_space = (2**(n-t) - 2) / 2
            cur_ans = []
            for num in layer:                
                for i in range(num_space):
                    cur_ans.append("")
                cur_ans.append(str(num.val) if num else "")
                for i in range(num_space):
                    cur_ans.append("")
                cur_ans.append("")
            cur_ans.pop(-1)
            ans.append(cur_ans)
        return ans
                    
root = TreeNode(1)
root.left = TreeNode(2)
print Solution().printTree(root)
            
