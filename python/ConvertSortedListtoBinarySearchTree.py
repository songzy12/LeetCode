# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param head, a list node
    # @return a tree node
    def sortedListToBST(self, head):
        l = []
        while head!=None:
            l.append(head.val)
            head = head.next
        return self.listToBST(l)
    def listToBST(self, l):
        if len(l)==0:
            return None
        if len(l)==1:
            return TreeNode(l[0])
        mid = len(l)//2
        head = TreeNode(l[mid])
        head.left = self.listToBST(l[:mid])
        head.right = self.listToBST(l[mid+1:])
        return head
    
##    def sortedListToBST(self, head):
##        i=0
##        pre = ListNode(0)
##        pre.next = head
##        while pre.next!=None:
##            pre = pre.next
##            i += 1
##        head = self.auxSortedListToBST(head, i)
##        return head
##    def auxSortedListToBST(self, head, L):
##        if L==0:
##            return None
##        if L==1:
##            return TreeNode(head.val)
##        else:
##            left = head
##            if L % 2 == 0:
##                for i in range(L//2):
##                    head = head.next
##                head_tree = TreeNode(head.val)
##                head_tree.left = self.auxSortedListToBST(left, L//2)
##                head_tree.right = self.auxSortedListToBST(head.next, L//2-1)
##                return head_tree
##            else:
##                for i in range((L-1)//2):
##                    head = head.next
##                head_tree = TreeNode(head.val)
##                head_tree.left = self.auxSortedListToBST(left, L//2)
##                head_tree.right = self.auxSortedListToBST(head.next, L//2)
##                return head_tree

nums = [1, 3]
dummy = point = ListNode(0)
for i in nums:
    point.next = ListNode(i)
    point = point.next
head = Solution().sortedListToBST(dummy.next)
print(head.left.val, head.val)
