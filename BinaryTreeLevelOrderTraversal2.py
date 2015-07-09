from Tree import *

class Solution:
    # @param root, a tree node
    # @return a list of lists of integers
    def levelOrderBottom(self, root):
        l=[]
        q=[]
        # you CANNOT write as l=q=[]
        q.append(root)
        q.append('#')
        # while q != ['#']
        while len(q)!=1:
            t=q[0]
            e=[]
            while t!='#':
                if t!=None:
                    e.append(t.val)
                    q.append(t.left)
                    q.append(t.right)
                q.remove(t)
                t=q[0]
            q.append('#')
            q.remove(t)
            # if e!=[]:
            if(len(e)!=0):
                l.append(e)
        l.reverse()
        return l

root=TreeNode(3)
root.left=TreeNode(9)
root.right=TreeNode(20)
root.right.left=TreeNode(15)
root.right.right=TreeNode(7)
print(Solution().levelOrderBottom(root))
