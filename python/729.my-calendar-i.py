# https://leetcode.com/problems/my-calendar-i/description/

class Node(object):
    def __init__(self, l, r):
        self.left = None
        self.right = None

        self.low = l
        self.high = r
        self.max = r

class MyCalendar(object):

    def __init__(self):
        self.root = None

    def overlap(self, l1, r1, l2, r2):
        # [l1, r1) and [l2, r2)
        if r1 <= l2 or r2  <= l1:
            return False
        return True
    
    def search(self, node, l, r):
        if node == None:
            return False

        if self.overlap(l, r, node.low, node.high):
            return True

        if node.left == None:
            return self.search(node.right, l, r)

        if node.left.max > l:
            # suppose no overlap,
            # then [a, node.left.max) must not overlap with [l, r)
            # so r <= a,
            # then there will not be overlap interval in right subtree
            return self.search(node.left, l, r)
        else:
            return self.search(node.right, l, r)

    def insert(self, node, l, r):
        if node == None:
            node = Node(l, r)
            return node

        if node.low >= l:
            node.left = self.insert(node.left, l, r)
        else:
            node.right = self.insert(node.right, l, r)

        # NOTE: remember to update the max field

        node.max = max(node.max, r)
        return node

    def in_order(self, node):
        if not node:
            return
        self.in_order(node.left)
        print('[%d, %d]' % (node.low, node.high))
        self.in_order(node.right)
            

    def book(self, start, end):
        """
        :type start: int
        :type end: int
        :rtype: bool
        """
        if self.root == None:
            self.root = Node(start, end)
            return True

        if self.search(self.root, start, end):
            return False

        self.root = self.insert(self.root, start, end)
        return True


# Your MyCalendar object will be instantiated and called as such:
obj = MyCalendar()

books = [[20,29],[13,22],[44,50],[1,7],[2,10],[14,20],[19,25],[36,42],[45,50],[47,50],[39,45],[44,50],[16,25],[45,50],[45,50],[12,20],[21,29],[11,20],[12,17],[34,40],[10,18],[38,44],[23,32],[38,44],[15,20],[27,33],[34,42],[44,50],[35,40],[24,31]]

# [null,true,false,true,true,false,true,false,true,false,false,false,false,false,false,false,false,false,false,false,false,false,false,false,false,false,false,false,false,false,false]

for start, end in books:
    print(obj.book(start,end))


# https://www.geeksforgeeks.org/interval-tree/
# https://www.youtube.com/watch?v=q0QOYtSsTg4
