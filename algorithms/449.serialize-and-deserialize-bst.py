# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        layer = [root]
        res = []
        while layer:
            next_layer = []
            for x in layer:
                if x:
                    next_layer += [x.left, x.right]
            temp = [x.val  if x else None for x in layer]
            res += temp
            layer = next_layer
        # print res
        return str(res)
            

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        l = eval(data)
        root = TreeNode(l[0]) if l[0] != None else None
        # 0 is not the same as None
        index = 1
        layer = [root]
        while layer:
            next_layer = []
            for node in layer:
                if node:
                    node.left = TreeNode(l[index]) if l[index] != None else None
                    index += 1
                    node.right = TreeNode(l[index]) if l[index] != None else None
                    index += 1
                    next_layer += [node.left, node.right]
            layer = next_layer
        return root
        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))
