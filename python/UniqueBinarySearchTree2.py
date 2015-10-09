from Tree import *

class Solution:
    # @return a list of tree node
    def generateTrees(self, n):
        if n<1:
            return [None]
        return self.auxGenerateTrees(1,n)
    def auxGenerateTrees(self, i, j):
        if i==j:
            return [TreeNode(i)]
        l=[]
        for m in range(i, j+1):
            if m==i:
                for y in self.auxGenerateTrees(m+1, j):
                    # notice the way to assign value
                    root=TreeNode(m)
                    root.right=y
                    l.append(root)
            elif m==j:
                for x in self.auxGenerateTrees(i,m-1):
                    root=TreeNode(m)
                    root.left=x
                    l.append(root)
            else:
                for x in self.auxGenerateTrees(i, m-1):
                    for y in self.auxGenerateTrees(m+1, j):
                        root=TreeNode(m)
                        root.left=x
                        root.right=y
                        l.append(root)
        return l

n=3
for x in Solution().generateTrees(n):
    printTree(x)


