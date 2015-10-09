from List import *

class Solution:
    # @param head, a ListNode
    # @return a ListNode
    def deleteDuplicates(self, head):
        if head==None:
            return None
        dummy=ListNode(0)
        dummy.next=head
        pre=post=head
        while True:
            while post.next!=None and post.val==post.next.val:
                post=post.next
            pre.next=post.next
            if post.next==None:
                return dummy.next
            pre=post=post.next

vals=[1,1,2,3,3]
printList(Solution().deleteDuplicates(initList(vals)))
