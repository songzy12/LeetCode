# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param {ListNode} head
    # @return {ListNode}
    def reverseList(self, head):
        if not head or not head.next:
            return head
        pre = head
        mid = pre.next
        pre.next = None
        while mid.next:
            post = mid.next
            mid.next = pre
            pre = mid
            mid = post
        mid.next = pre
        return mid

head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head = Solution().reverseList(head)
while head:
    print(head.val, end=' ')
    head = head.next
            

            
