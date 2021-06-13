# Definition for singly-linked list with a random pointer.
class RandomListNode:
    def __init__(self, x):
        self.label = x
        self.next = None
        self.random = None

class Solution:
    # @param head, a RandomListNode
    # @return a RandomListNode
    def copyRandomList(self, head):
        if not head: # NOTICE!
            return None
        m = {}
        new_head = RandomListNode(head.label)
        cur0 = head
        cur1 = new_head
        while cur0.next:
            m[cur0] = cur1
            cur1_next = RandomListNode(cur0.next.label)
            cur1.next = cur1_next
            cur0 = cur0.next
            cur1 = cur1.next
        m[cur0] = cur1
        m[None] = None
        cur0 = head
        cur1 = new_head
        while cur0:
            cur1.random = m[cur0.random]
            cur0 = cur0.next
            cur1 = cur1.next
        return new_head

nodes = [RandomListNode(i) for i in range(5)]
for i in range(4):
    nodes[i].next = nodes[i+1]
    nodes[i].random = nodes[(i+3)%5]
head = nodes[0]
new_head = Solution().copyRandomList(head)
while head.next:
    print(head.label, head.next.label, head.random.label)
    head = head.next
print()
while new_head.next:
    print(new_head.label, new_head.next.label, new_head.random.label)
    new_head = new_head.next
