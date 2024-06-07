# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: void Do not return anything, modify head in-place instead.
        """
        if not head:
            return
        stack = []
        slow = fast = ListNode(0)
        slow.next = fast.next = head
        while fast.next and fast.next.next:
            slow = slow.next
            stack += slow,
            fast = fast.next.next
        # now stack contains the first half of nodes
        next_node = None
        slow = slow.next
        if fast.next: # odd
            next_node = slow
            slow = slow.next
            next_node.next = None
        # slow now is the head of second half
        while slow:
            cur = stack.pop()
            print cur.val, slow.val
            temp = slow.next
            slow.next = next_node
            cur.next = slow
            next_node = cur
            slow = temp

##        l = 0
##        cur = head
##        while cur:
##            l += 1
##            cur = cur.next
##        self.reorderHelper(head, l)
##
##    def reorderHelper(self, node, length):
##        if length == 1:
##            temp = node.next
##            node.next = None
##            return temp
##        if length == 2:
##            temp = node.next.next
##            node.next.next = None
##            return temp
##        next_node = self.reorderHelper(node.next, length-2)
##        temp = next_node.next
##        next_node.next = node.next
##        node.next = next_node
##        return temp

node = [ListNode(i) for i in range(1,2)]
    
head = node[0]
Solution().reorderList(None)
while head:
    print head.val,
    head = head.next
    
    
        
        
        
