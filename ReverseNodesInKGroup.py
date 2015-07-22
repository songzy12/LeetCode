# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param {ListNode} head
    # @param {integer} k
    # @return {ListNode}
    def reverseKGroup(self, head, k):
        if not head:
            return head
        dummy, dummy.next = ListNode(0), head
        Front, front = dummy, dummy.next
        while front:
            cur,pos = front,front.next
            cond = True
            temp = pos
            for i in range(k-1):
                if not temp:
                    cond = False
                    break
                temp = temp.next
            if not cond:
                break
            for i in range(k-1):
                #if not pos:
                #    break
                pre = cur
                cur = pos
                pos = cur.next
                cur.next = pre
            Front.next = cur
            Front = front
            front = pos
        # Front.next = None
        Front.next = front
        return dummy.next

def print_list(node):
    while node:
        print(node.val, end = " ")
        node = node.next
    print()

node1 = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(3)
node4 = ListNode(4)
node5 = ListNode(5)
node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5
print_list(node1)
node = Solution().reverseKGroup(node1, 4)
print_list(node)

    
