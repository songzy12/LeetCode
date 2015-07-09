class Solution:
    # @param a ListNode
    # @return a ListNode
    def swapPairs(self, head):
        dummy=ListNode(0)
        dummy.next=head
        tmp=dummy        
        while tmp.next!=None and tmp.next.next!=None:
            tmp1=tmp.next
            tmp2=tmp1.next
            # tmp->tmp1->tmp2->
            # tmp->tmp2->tmp1->
            tmp.next=tmp2
            tmp1.next=tmp2.next
            tmp2.next=tmp1
            tmp=tmp1
        return dummy.next

from List import *
vals=[1,2,3,4]
printList(Solution().swapPairs(initList(vals)))

