# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param {ListNode} node
    # @return {void} Do not return anything, modify node in-place instead.
    def deleteNode(self, node):
        node.val = node.next.val
        node.next = node.next.next
##        while node.next.next:
##            node.val = node.next.val
##            node = node.next
##        node.val = node.next.val
##        node.next = None

node1 = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(3)
node4 = ListNode(4)
node1.next = node2
node2.next = node3
node3.next = node4

def printNode(node):
    while node:
        print(node.val, end = " ")
        node = node.next
    print()

printNode(node1)
Solution().deleteNode(node3)
printNode(node1)    
