from List import *
# try no extra space, when you are free
class Solution:
    # @param head, a ListNode
    # @return a list node
    def detectCycle(self, head):
        d={}
        while head!=None:
            if head in d:
                return head
            d[head]=1
            head=head.next
        return None

head=ListNode(1)
head.next=ListNode(2)
head.next.next=ListNode(3)
head.next.next.next=head
print(Solution().detectCycle(head).val)
        
