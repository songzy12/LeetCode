class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class BSTIterator:
    # @param root, a binary search tree's root node
    def __init__(self, root):
        self.q = list()
        self.pushAll(root)
        

    # @return a boolean, whether we have a next smallest number
    def hasNext(self):
        return True if self.q else False

    # @return an integer, the next smallest number
    def next(self):
        temp = self.q.pop()
        self.pushAll(temp.right)
        return temp.val

    def pushAll(self, root):
        while root:
            self.q.append(root)
            root = root.left

root = None
test = BSTIterator(root)
while test.hasNext():
    print(test.next())

