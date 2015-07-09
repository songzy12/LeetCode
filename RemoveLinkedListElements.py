# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param {ListNode} head
    # @param {integer} val
    # @return {ListNode}
    def removeElements(self, head, val):
        dum = pre = ListNode(0)
        dum.next = head
        while pre and pre.next:
            if pre.next.val == val:
                pre.next = pre.next.next
            else:
                pre = pre.next
        return dum.next

head = ListNode(1)
head.next = ListNode(1)
head = Solution().removeElements(head, 1)
while head:
    print(head.val, end = " ")
    head = head.next
    
