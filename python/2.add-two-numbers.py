# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @return a ListNode
    def addTwoNumbers(self, l1, l2):
        dummy = pre = ListNode(0)
        dummy1 = ListNode(0)
        dummy2 = ListNode(0)
        carry = 0
        dummy1.next = l1
        dummy2.next = l2
        
        while dummy1.next and dummy2.next:
            dummy1 = dummy1.next
            dummy2 = dummy2.next
            v = dummy1.val + dummy2.val + carry
            carry = 0 if v < 10 else 1
            v = v if v < 10 else v - 10
            post = ListNode(v)
            pre.next = post
            pre = post
        
        while dummy1.next:
            dummy1 = dummy1.next
            v = dummy1.val + carry
            carry = 0 if v < 10 else 1
            v = v if v < 10 else v - 10
            post = ListNode(v)
            pre.next = post
            pre = post
        while dummy2.next:
            dummy2 = dummy2.next
            v = dummy2.val + carry
            carry = 0 if v < 10 else 1
            v = v if v < 10 else v - 10
            post = ListNode(v)
            pre.next = post
            pre = post
        if carry:
            post = ListNode(carry)
            pre.next = post
        return dummy.next

l1 = ListNode(5)
l2 = ListNode(5)

l = Solution().addTwoNumbers(l1, l2)
while l:
    print (l.val, end=' ')
    l = l.next
