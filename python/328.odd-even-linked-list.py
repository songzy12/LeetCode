# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def oddEvenList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return head
        odd_cur = odd_head = head
        even_cur = even_head = head.next
        while even_cur and even_cur.next:
            odd_cur.next = even_cur.next
            even_cur.next = even_cur.next.next
            odd_cur = odd_cur.next
            even_cur = even_cur.next
        odd_cur.next = even_head
        return odd_head
        
nodes = [ListNode(i) for i in range(3)]
for i in range(2):
    nodes[i].next = nodes[i+1]
head = Solution().oddEvenList(nodes[0])
while head:
    print head.val,
    head = head.next
    
