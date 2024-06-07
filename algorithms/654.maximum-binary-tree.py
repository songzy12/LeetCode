# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def constructMaximumBinaryTree(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        stack = []
        for num in nums:
            if not stack:
                stack.append(TreeNode(num))
                continue
            if stack[-1].val > num:
                stack.append(TreeNode(num))
                continue

            cur_node = TreeNode(num)
            cur_list = []
            while stack and stack[-1].val < num:
                cur_list.append(stack.pop(-1))
            for i in range(len(cur_list)-1):
                cur_list[i+1].right = cur_list[i]

            cur_node.left = cur_list[-1]
            stack.append(cur_node)
        for i in range(len(stack)-1):
            stack[i].right = stack[i+1]
        return stack[0]
            
nums = [3,2,1,6,0,5]
print Solution().constructMaximumBinaryTree(nums)
                
                
        
