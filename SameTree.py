from Tree import *
class Solution:
    # @param p, a tree node
    # @param q, a tree node
    # @return a boolean


    def isSameTree(self,p,q):
        # be careful about what 'same structure' means
        if p==None or q==None:
            return p==q
        else:
            return p.val==q.val and self.isSameTree(p.left,q.left) and self.isSameTree(p.right,q.right)

    
##    def isSameTree(self, p, q):
##        pList=self.preOrder(p)
##        qList=self.preOrder(q)
##        if len(pList)!=len(qList):
##            return False
##        for i in xrange(len(pList)):
##            if pList[i]!=qList[i]:
##                return False
##        return True
##
##    def preOrder(self,p):
##        if p==None:
##            return []
##        l=[]
##        l.extend(self.preOrder(p.left))
##        l.extend([p.val])
##        l.extend(self.preOrder(p.right))
##        return l

print(Solution().isSameTree(initTree([1,1]),initTree([1,'#',1])))

        
