# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param two ListNodes
    # @return the intersected ListNode
    def getIntersectionNode(self, headA, headB):
##        d={}
##        while headA!=None:
##            d[headA]=0
##            headA=headA.next
##        while headB!=None:
##            # TLE, O(1) memory
##            if headB in d.keys():
##                return headB
##            headB=headB.next
##        return None

##        headA_=ListNode(0)
##        headA_.next=headA
##        headB_=ListNode(0)
##        headB_.next=headB
##        while headA_.next!=None:
##            temp=headA_.next
##            headA_.next=None
##            headA_=temp
##        while headB_.next!=None:
##            headB_=headB_.next
##        return None if headB_!=headA_ else headB_

        # the point is that once intersected
        # what remains are all the same
        # so we first compute the difference of length
        # then come to the same position from end
        # check them one by one
        l1=l2=0
        tmp = headA
        while tmp!=None:
            l1 = l1+1
            tmp = tmp.next
        tmp = headB
        while tmp!=None:
            l2 = l2+1
            tmp = tmp.next
        if l1<l2:
            for i in range(l2-l1):
                headB=headB.next
        if l2<l1:
            for i in range(l1-l2):
                headA=headA.next
        while headA!=None:
            if headA==headB:
                return headA
            headA=headA.next
            headB=headB.next
        return None


Node1=ListNode(1)
Node2=ListNode(2)
Node3=ListNode(3)
headA=Node1
headA.next=Node3
headB=Node2
headB.next=Node3
print(Solution().getIntersectionNode(headA, headB).val)
            
