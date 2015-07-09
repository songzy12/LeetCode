class LRUCache:
    class Node:
        def __init__(self, key, value):
            self.key = key
            self.value = value
            self.next = None
            self.pre = None
    # @param capacity, an integer
    def __init__(self, capacity):
        self.capacity = capacity
        # size can be replaced by len(m)
        self.head = self.Node(0, -1)
        self.tail = self.Node(0, -1)
        self.head.next = self.tail
        self.tail.pre = self.head
        self.m = {} # use m to hash Node rather than value

    # @return an integer
    def get(self, key):
        if key not in self.m:
            return -1
        cur = self.m[key] # use hash rather than loop
        cur.pre.next = cur.next
        cur.next.pre = cur.pre
        self.head.next.pre = cur
        cur.next = self.head.next
        self.head.next = cur
        cur.pre = self.head
        return cur.value

    # @param key, an integer
    # @param value, an integer
    # @return nothing
    def set(self, key, value):
        if key not in self.m:
            cur = self.Node(key, value)
            if len(self.m) == self.capacity:
                self.m.pop(self.tail.pre.key)
                self.tail.pre = self.tail.pre.pre
                self.tail.pre.next = self.tail

            cur.next = self.head.next
            self.head.next.pre = cur
            self.head.next = cur
            cur.pre = self.head
            self.m[key] = cur
        else:
            cur = self.m[key]
            cur.pre.next = cur.next
            cur.next.pre = cur.pre

            cur.next = self.head.next
            self.head.next.pre = cur
            self.head.next = cur
            cur.pre = self.head
            cur.value = value
            

def printCache(c):
    cur = c.head
    while cur:
        print(cur.key, cur.value)
        cur = cur.next

c = LRUCache(2)
print(c.get(2))
c.set(2,6)
# printCache(c)
# print(c.m)
print(c.get(1))
c.set(1,5)
# printCache(c)
# print(c.m)
c.set(1,2)
# printCache(c)
# print(c.m)
print(c.get(1))
print(c.get(2))
