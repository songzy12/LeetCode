# https://en.wikipedia.org/wiki/Reservoir_sampling
# Given a singly linked list, return a random node's value from the linked list.
# Each node must have the same probability of being chosen.

import random


class ListNode(object):
    # Definition for singly-linked list.
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
        current = self.head
        result_size = 1
        result = []
        n = 1
        while len(result) < result_size:
            result.append(current)
            current = current.next
            n += 1

        while current:
            index = random.randrange(0, n)
            if index < result_size:
                result[index] = current
            current = current.next
            n += 1
        return result[0].val

# Your Solution object will be instantiated and called as such:
# obj = Solution(head)
# param_1 = obj.getRandom()

# first thought: no thought
# count the length, sample the random % size() th node. note lazy initialization
# reservoir sampling: if random.randint(0, n-1) == 0, then select
