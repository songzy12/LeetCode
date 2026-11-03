# https://leetcode.com/problems/add-two-numbers-ii/description/

from List import ListNode


class Solution:

    def addTwoNumbers(self, l1: ListNode | None,
                      l2: ListNode | None) -> ListNode | None:
        l1 = self.reverseList(l1)
        l2 = self.reverseList(l2)
        return self.reverseList(self.addTwoNumbersReversed(l1, l2))

    def reverseList(self, head):
        prev = None
        while head:
            next_node = head.next
            head.next = prev
            prev = head
            head = next_node
        return prev

    def addTwoNumbersReversed(self, l1, l2):
        head = cur = ListNode(0)
        carry = 0

        while l1 and l2:
            val, carry = self.computeValAndCarry(l1.val, l2.val, carry)

            cur.next = ListNode(val)

            cur = cur.next
            l1 = l1.next
            l2 = l2.next

        while l1:
            val, carry = self.computeValAndCarry(l1.val, 0, carry)

            cur.next = ListNode(val)

            cur = cur.next
            l1 = l1.next

        while l2:
            val, carry = self.computeValAndCarry(0, l2.val, carry)

            cur.next = ListNode(val)

            cur = cur.next
            l2 = l2.next

        if carry:
            cur.next = ListNode(carry)

        return head.next

    def computeValAndCarry(self, val1, val2, carry):
        val = val1 + val2 + carry
        return val % 10, val // 10
