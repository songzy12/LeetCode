from List import *
class Solution:
    # @param head, a ListNode
    # @return a boolean
    def hasCycle(self, head):
        
        if head == None or head.next==None:
            return False
        # the idea is to reverse the list
        # just draw a graph then you will know
        prev=None
        cur=head
        while cur != None:
            # None <- prev    cur -> cur.next ->
            # None <- prev <- cur    cur.next ->
            tmp = cur.next
            cur.next = prev
            prev = cur
            cur = tmp
        ans=False
        if prev == head:
            ans=True
##
##        # just to recover the structure
##        head = prev
##        prev = None
##        cur = head
##        while cur != None:
##            tmp = cur.next
##            cur.next = prev
##            prev = cur
##            cur = tmp
##        head = prev
        return ans


##        # modify the pointer
##        while head!=None:
##            if head.next==head:
##                return True
##            tmp=head.next
##            head.next=head
##            head=tmp
##        return False
    

##        # the idea is that if cycle exists
##        # fast will finally catch up with slow
##        slow=fast=head        
####        i=0
####        while fast!=None:
####            if i%2:
####                slow=slow.next
####            fast=fast.next
####            i+=1
####            if slow==fast:
####                return True
####        return False
##        while fast!=None and fast.next!=None:
##            fast=fast.next.next
##            slow=slow.next
##            if slow==fast:
##                return True
##        return False

##        # this is rather slow
##        # dir() and .tag costs time
##        while head!=None:
##            if 'tag' in dir(head):
##                return True
##            else:
##                head.tag=True
##                head=head.next
##        return False
        

n1=ListNode(1)
n2=ListNode(2)
n3=ListNode(3)
n1.next=n2
n2.next=n3
n3.next=n1
##n1=None
print(Solution().hasCycle(n1))

            
            
        
