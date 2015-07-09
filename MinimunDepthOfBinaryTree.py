from Tree import *
class Solution:
    # @param root, a tree node
    # @return an integer
    def minDepth(self, root):
        if root==None:
            return 0
        # to use list instead of queue
        l=list()
        l.append(root)
##        # Queue imported to use queue
##        import Queue
##        queue=Queue.Queue()
##        queue.put(root)
        cur=height=1
        # height denotes the current level depth
        # cur denotes No. nodes left of current level
        nxt=0
        # nxt denotes No. nodes of next level
        while len(l)!=0:            
##        while not queue.empty():
            top=l[0]
            del l[0]
##            top=queue.get()
            # when get a node, No. nodes of current level decrease
            cur-=1
            # when come across a leaf node
            if top.left==None and top.right==None:
                return height
            if top.left!=None:
                # put the child into queue, add No. of next level
                l.append(top.left)
##                queue.put(top.left)
                nxt+=1
            if top.right!=None:
                l.append(top.right)
##                queue.put(top.right)
                nxt+=1
            if cur==0:
                # when current level is over, turn into next level
                cur=nxt
                nxt=0
                height+=1


##    # another solution using prune technique
##    min_depth=2**31-1
##    def minDepth(self, root):
##        if root==None:
##            return 0
##        # when the root is not none
##        self.minHelper(root,0)
##        return self.min_depth
##    def minHelper(self, root, depth):
##        # prune when the depth goes too far
##        if depth>=self.min_depth:
##            return
##        # if it is a leaf, then min_depth gets smaller
##        if root.left==None and root.right == None:
##            self.min_depth=depth+1
##            return
##        # if it has children, depth++  
##        if root.left:
##            self.minHelper(root.left,depth+1)
##        if root.right:
##            self.minHelper(root.right,depth+1)

            
##        # record the depth of left and right
##        # use pre-order traverse
##        left=self.minDepth(root.left)
##        right=self.minDepth(root.right)
##        # if this is a leaf node
##        if left==0 and right==0:
##            return 1
##        # if only have right leaf
##        if left==0:
##            return 1+right
##        # if only have left leaf
##        if right==0:
##            return 1+left
##        return 1+min(left,right)
                
    
##    def minDepth(self, root):
##        if root == None:
##            return 0
####        if root.left==None and root.right==None:
####            return 1
####        if root.left==None:
####            return self.minDepth(root.right)+1
####        if root.right==None:
####            return self.minDepth(root.left)+1
##        if root.left==None or root.right==None:
##            return self.minDepth(root.left)+self.minDepth(root.right)+1
##        return min(self.minDepth(root.right),self.minDepth(root.left))+1


print(Solution().minDepth(initTree([1,2])))

