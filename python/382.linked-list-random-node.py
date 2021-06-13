# Given a singly linked list, return a random node's value from the linked list.
# Each node must have the same probability of being chosen.

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):

    def __init__(self, head):
        """
        @param head The linked list's head.
        Note that the head is guaranteed to be not null, so it contains at least one node.
        :type head: ListNode
        """
        self.head = head        

    def getRandom(self):
        """
        Returns a random node's value.
        :rtype: int
        """
        result = None
        current = self.head
        n = 1
        while current:
            if random.randint(0, n - 1) == 0:
                result = current
            current = current.next
            n += 1
        return result.val

# Your Solution object will be instantiated and called as such:
# obj = Solution(head)
# param_1 = obj.getRandom()

# first thought: no thought
# count the length, sample the random % size() th node. note lazy initialization
# reservoir sampling: if random.randint(0, n-1) == 0, then select
