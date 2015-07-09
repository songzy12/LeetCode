from List import *
class Solution:
    # @param head, a ListNode
    # @param k, an integer
    # @return a ListNode
    def rotateRight(self, head, k):
        # {},1
        if head==None:
            return None
        # {1},1
        dummyHead=ListNode(0)
        dummyHead.next=head
        tmp=dummyHead
        count=0
        while tmp.next!=None:
            tmp=tmp.next
            count+=1
        #{1,2},2
        k=k%count
        if k==0:
            return head
        
        fast=slow=dummyHead
        for i in range(k):
            fast=fast.next
        while fast.next!=None:
            fast=fast.next
            slow=slow.next
        fast.next=head
        tmp=slow.next
        slow.next=None
        return tmp

vals=[1,2,3]
k=2
printList(Solution().rotateRight(initList(vals),k))
