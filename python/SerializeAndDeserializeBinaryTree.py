# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        return str(self.serializeHelper(root, []))
    
    def serializeHelper(self, root, res):
        if not root:
            res += None,
            return res
        res += root.val,
        self.serializeHelper(root.left, res)
        self.serializeHelper(root.right, res)
        return res
    
    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        data = eval(data)
        return self.deserializeHelper(data)
    
    def deserializeHelper(self, data):
        if not data:
            return None
        temp = data.pop(0)
        if temp == None:
        # if not temp: 
            return None
        root = TreeNode(temp)
        root.left = self.deserializeHelper(data)
        root.right = self.deserializeHelper(data)
        return root
        

# Your Codec object will be instantiated and called as such:

root = TreeNode(0)
root.left = TreeNode(1)
root.right = TreeNode(2)
root.left.left = TreeNode(3)
root.right.left = TreeNode(4)

codec = Codec()
root = codec.deserialize(codec.serialize(root))
    
