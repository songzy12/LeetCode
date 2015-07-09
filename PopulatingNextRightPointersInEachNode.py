# Definition for binary tree with next pointer.
class TreeLinkNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        self.next = None

class Solution:
    # @param root, a tree link node
    # @return nothing
    def connect(self, root):
        if root == None:
            return None
        pre = root
        cur = None
        while pre.left:
            # pre is the left most node on each level
            cur = pre
            # the idea is when on level cur,
            # modify the pointers of next level
            while cur.next:
                cur.left.next = cur.right
                cur.right.next = cur.next.left
                cur = cur.next
            cur.left.next = cur.right
            pre = pre.left
        return None
    
##        if root == None:
##            return None
##        queue = [root]
##        size = 1
##        while queue[0] != None:
##            current = []
##            current[:] = queue[:]
##            queue = []
##            for i in current:
##                queue.append(i.left)
##                queue.append(i.right)
##            for i in range(size-1):
##                current[i].next = current[i+1]
##            size = size * 2
##        return None

node0=TreeLinkNode(0)
node1=TreeLinkNode(1)
node2=TreeLinkNode(2)
node3=TreeLinkNode(3)
node4=TreeLinkNode(4)
node5=TreeLinkNode(5)
node6=TreeLinkNode(6)
node0.left = node1
node0.right = node2
node1.left = node3
node1.right = node4
node2.left = node5
node2.right = node6
Solution().connect(node0)
print(node3.next.val, node4.next.val, node5.next.val, node6.next == None)
        
