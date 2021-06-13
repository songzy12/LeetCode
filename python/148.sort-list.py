# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return
        if not head.next:
            return head
        slow = fast = ListNode(0)
        slow.next = fast.next = head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        l = self.sortList(slow.next)
        slow.next = None
        r = self.sortList(head)
        cur = dummy = ListNode(0)
        while l and r:
            if l.val < r.val:
                cur.next = l
                l = l.next
            else:
                cur.next = r
                r = r.next
            cur = cur.next
        while l:
            cur.next = l
            cur, l = cur.next, l.next
        while r:
            cur.next = r
            cur, r = cur.next, r.next
        return dummy.next

node = [ListNode(7-i) for i in range(1, 7)]
for i in range(5):
    node[i].next = node[i+1]

head = Solution().sortList(node[0])
while head:
    print head.val,
    head = head.next
