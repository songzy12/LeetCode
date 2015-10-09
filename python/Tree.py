# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def initTree(vals):
    # remember to complete this when you are free
    if len(vals)==0:
        return None
    root=TreeNode(vals.pop(0))
    q=[root]
    while len(vals)>0:
        tmpNode=q.pop(0)
        tmpVal=vals.pop(0)
        if tmpVal!='#':
            tmpNode.left=TreeNode(tmpVal) 
        tmpVal=vals.pop(0) if len(vals)>0 else '#'
        if tmpVal!='#':
            tmpNode.right=TreeNode(tmpVal) 
        q.extend([tmpNode.left, tmpNode.right])
    return root

def printTree(root):
    l=[]
    queue=[root]
    while len(queue)!=0:
        tmp=queue[0]
        if tmp==None:
            l.append('#')
            queue.remove(tmp)
            continue
        l.append(tmp.val)
        queue.append(tmp.left)
        queue.append(tmp.right)
        queue.remove(tmp)
    for i in range(len(l)-1,-1,-1):
        if l[i]=='#':
            l.pop(i)
        else:
            break
    print(l)
