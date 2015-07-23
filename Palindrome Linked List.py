# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param {ListNode} head
    # @return {boolean}
    def isPalindrome(self, head):
        # use fast and slow, slow = slow.next, fast = fast.next.next
        # when fast meets the end, slow is right in the middle
        if not head or not head.next:
            return True
        count = 1
        pre = head
        cur,pre.next = pre.next,None
        while cur:
            count += 1
            post, cur.next, pre = cur.next, pre, cur
            cur = post
        half = count // 2 - 1
        cur, pre.next = pre.next, None
        while half:
            half -= 1
            post,cur.next,pre = cur.next,pre,cur
            cur = post
        head1 = pre
        head2 = cur.next if count % 2 else cur
        # print(head1.val, head2.val)
        while head1:
            if head1.val != head2.val:
                break
            head1, head2 = head1.next, head2.next
        if head1:
            return False
        return True

N = 2
nodes = [ListNode(i) for i in range(N)] + [ListNode(11)] + \
        [ListNode(i) for i in range(N-1, -1, -1)]
for i in range(2*N):
    nodes[i].next = nodes[i+1]
print(Solution().isPalindrome(nodes[0]))
