# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """
        if not head:
            return head
        dummy = ListNode(0)
        dummy.next = head
        cur = dummy
        for i in range(m-1):
            cur = cur.next
        # cur is now the previous node of m
        pre_n = cur # Pre.next = n
        node_m = pre = cur.next # node_m.next = n.next
        cur = node_m.next
        
        for i in range(n-m):
            post = cur.next
            cur.next = pre
            pre = cur
            cur = post
        # pre = node_n, cur = node_n.next
        pre_n.next = pre
        node_m.next = cur
        return dummy.next
        
node = [ListNode(i+1) for i in range(5)]
for i in range(4):
    node[i].next = node[i+1]
m, n = 1, 1
head = Solution().reverseBetween(ListNode(1), m, n)
while head:
    print head.val,
    head = head.next
