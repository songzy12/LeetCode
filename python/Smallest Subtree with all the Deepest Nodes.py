# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, son):
#         self.val = son
#         self.left = None
#         self.right = None

class Solution(object):
    def __init__(self):
        self.depth = {}
        self.deepest = 0

        self.depth_cnt = {}

        self.cur_ans = None
        self.cur_depth = 0

    def subtreeWithAllDeepest(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        self.depth[root] = 0
        def get_depth(node):
            for son in [node.left, node.right]:
                if son:
                    self.depth[son] = self.depth[node] + 1
                    if self.depth[son] > self.deepest:
                        self.deepest = self.depth[son]
                    get_depth(son)
        get_depth(root)
        #print({k.val: v for k, v in self.depth.items() if k})

        def check_deep(node):
            if not node:
                self.depth_cnt[node] = 0
                return 0
            
            if self.depth[node] == self.deepest:
                self.depth_cnt[node] = 1
                return 1

            for son in [node.left, node.right]:
                check_deep(son)
            self.depth_cnt[node] = self.depth_cnt[node.left] + self.depth_cnt[node.right]
            return self.depth_cnt[node]

        depth_cnt = check_deep(root)
        #print({k.val: v for k, v in self.depth_cnt.items() if k})

        self.cur_ans = root
        def find_ans(node):
            if not node:
                return 
            if self.depth_cnt[node] < self.depth_cnt[root]:
                return 
            if self.depth[node] > self.cur_depth:
                self.cur_depth = self.depth[node]
                self.cur_ans = node
            find_ans(node.left)
            find_ans(node.right)
        find_ans(root)
        return self.cur_ans