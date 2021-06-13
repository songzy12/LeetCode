from List import *
class Solution:
    # @return a ListNode
    def removeNthFromEnd(self, head, n):
        # the idea is that n+x=x+n
        # that is awsome!!!
        dummyHead=ListNode(0)
        dummyHead.next=head
        fast=slow=dummyHead
        for i in range(n):
        # xrange() merge into range()
            fast=fast.next
            # fast go through n elements
        while fast.next!=None:
            fast=fast.next
            slow=slow.next
            # n elements left for slow
        slow.next=slow.next.next
        return dummyHead.next

        
##        list1=[]
##        # make a list to refer to later
##        count=0
##        preHead=ListNode(0)
##        preHead.next=head
##        while head!=None:
##            count+=1
##            list1.append(head)
##            head=head.next
##        if count-n-1<0:
##            # if the one is the first
##            return preHead.next.next
##        else:
##            pre=list1[count-n-1]
##            tmp=pre.next
##            pre.next=tmp.next
##            tmp.next=None
##        return preHead.next

vals=[1,2,3,4,5]
n=2
printList(Solution().removeNthFromEnd(initList(vals),n))
