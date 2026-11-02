# https://leetcode.com/problems/add-two-numbers/description/


class ListNode:

    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:

    def addTwoNumbers(self, l1, l2):
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


def printList(head):
    while head:
        print(head.val, end=" ")
        head = head.next
    print()


if __name__ == "__main__":
    l1 = ListNode(5)
    l2 = ListNode(5)

    printList(Solution().addTwoNumbers(l1, l2))
