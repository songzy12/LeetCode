from List import *

class Solution:
    # @param head, a ListNode
    # @param k, an integer
    # @return a ListNode
    def reverseKGroup(self, head, k):
        dummy=ListNode(0)
        dummy.next=head
        pre=post=head
        for i in range(k):
            

vals=[1,2,3,4,5]
for k in 2,3:
    printList(Solution().reverseKGroup(initList(vals),k))
