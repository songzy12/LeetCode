from List import *
class Solution:
    # @param head, a ListNode
    # @param x, an integer
    # @return a ListNode
    def partition(self, head, x):

##        # use extra space to store notices ge x
##        # again notice the trick of dummy
##        dummy=ListNode(0)
##        dummy.next=head
##        pointer=dummy
##        
##        dummynew=ListNode(0)
##        pointernew=dummynew
##        
##        while pointer.next!=None :
##            if pointer.next.val<x:
##                pointer=pointer.next
##            else:
##            # ->pointer->pointer.next->
##            # ->...
##            # to ->pointer.next->...
##            # to ->pointer->...
##                tmp=pointer.next
##                pointer.next=tmp.next
##                pointernew.next=tmp
##                tmp.next=None
##                pointernew=pointernew.next
##        pointer.next=dummynew.next
##        return dummy.next

        # use a dummy variant in case head is modified
        dummy=ListNode(0)
        dummy.next=head
        pre=post=dummy
        # test post.next.val to save variant post0
        while post!=None and post.next!=None:
            if post.next.val >=x:
                post=post.next
            # post is always >=x, then we can cite post.next<x
            else:
                # while pre==post, means while pre.next<x
                if pre==post:
                    # this is for the beginning
                    pre=pre.next
                    post=post.next
                # until we have pre<x, pre.next>=x,post>=x,post.next<x
                else:
                    # ->...->pre->pre.next->...->post->post.next->...
                    # fix to ...->pre->post.next->pre.next->...->pre.next
                    # use tmp to simplify the process of pointer change
                    tmp=post.next
                    post.next=tmp.next
                    tmp.next=pre.next
                    pre.next=tmp
                    pre=tmp
        # after the first round: dummy->pre->head->post
        return dummy.next

            
##        if head.val>=x:
##            # when input is {2,1,3},2
##            # need to do the first step by hand
##            pre0=None 
##            pre=head
##            
##            post0=pre
##            post=post0.next
##            if post==None:
##                return head
##            while post.val>=x:
##                post=post.next
##                post0=post0.next
##                if post==None:
##                    return head
##            # pre->...->post0->post->...
##
##            # fix to post->pre->...->post0->...
##            post0.next=post.next
##            head=post
##            post.next=pre
##            # then pre0=post, post=post0.next
##            # pre0->pre->...->post0->post->...
##            pre0=post
##            post=post0.next
##            # now pre0 is not None any more
##            
##        else:
##            pre0=head
##            pre=pre0.next
##            if pre==None:
##                return head                    
##            while pre.val<x:
##                pre=pre.next
##                pre0=pre0.next
##                if pre==None:
##                    return head
##       
##            post0=pre
##            post=post0.next
##            
##
##        while post!=None:
##            
##            while post.val>=x:
##                post=post.next
##                post0=post0.next
##                if post==None:
##                    return head
##            # now ...->pre0->pre->...->post0->post->...
##            # fix to ...->pre0->post-> pre->...->post0->...
##            # here pre0<x, pre>=x, post0>=x, post<x
##            post0.next=post.next
##            pre0.next=post
##            post.next=pre
##            # then pre0=post, post=post0.next
##            # ...->pre0->pre->...->post0->post->... again
##            pre0=post
##            post=post0.next
##            
##        return head

vals=[2,1,3]
x=2
printList(Solution().partition(initList(vals),x))
