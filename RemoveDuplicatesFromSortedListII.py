# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return head
        dummy = ListNode(0)
        dummy.next = head
        cur = dummy
        repeat = False
        while cur.next and cur.next.next:
            if cur.next.val == cur.next.next.val:
                cur.next = cur.next.next
                repeat = True
                continue
            if repeat:
                cur.next = cur.next.next
                repeat = False
                continue
            cur = cur.next
        if repeat:
            cur.next = None
        return dummy.next

node = [ListNode(1), ListNode(1), ListNode(1), ListNode(3), ListNode(3), ListNode(5), ListNode(5)]
for i in range(len(node)-1):
    node[i].next = node[i+1]
head = Solution().deleteDuplicates(node[0])
while head:
    print head.val,
    head = head.next
