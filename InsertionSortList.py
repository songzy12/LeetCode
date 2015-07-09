from List import *
class Solution:
    # @param head, a ListNode
    # @return a ListNode
    def insertionSortList(self, head):
        dummyHead=ListNode(0)
        tmp1=dummyHead.next=head
        while tmp1!=None and tmp1.next!=None:
            if tmp1.val>tmp1.next.val:
                tmp=tmp1.next
                tmp2=dummyHead
                while tmp2.next.val<tmp.val:
                    tmp2=tmp2.next
                tmp1.next=tmp.next
                tmp.next=tmp2.next
                tmp2.next=tmp
            else:
                tmp1=tmp1.next
        return dummyHead.next

vals=[3,2,1]
printList(Solution().insertionSortList(initList(vals)))
    
    
        
