# Definition for singly-linked list.

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def initList(vals):
    dummy=ListNode(0)
    tmp=dummy
    for x in vals:
        tmp.next=ListNode(x)
        tmp=tmp.next
    return dummy.next

def printList(head):
    while head!=None:
        print(head.val,end=" ")
        head=head.next
