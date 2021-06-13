class ListNode(object):
    def __init__(self, key, val):
        self.prev = None
        self.next = None
        self.val = val
        self.key = key

    def connect(self, nextNode):
        self.next = nextNode
        nextNode.prev = self

class LFUCache(object):

    def __init__(self, capacity):
        """
        
        :type capacity: int
        """
        self.cap = capacity
        self.head = ListNode(None, None)
        self.tail = ListNode(None, None)
        self.head.connect(self.tail)
        #use to record the first ListNode of this count number
        self.cnt = {0: self.tail}
        # key: key , value:[ListNode, visit count]
        self.kv = {None:[self.tail, 0]}

    def moveforward(self, key):
        node, cnt = self.kv[key]
        # set cnt to be cnt + 1
        # move it to be the first of nodes with cnt + 1
        # reuse add method
        self.add('tmp', node.val, cnt + 1)
        self.remove(key)
        self.kv[key] = self.kv['tmp']
        self.kv[key][0].key = key
        del self.kv['tmp']

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key not in self.kv:
            return -1
        self.moveforward(key)
        # key: key , value:[ListNode, visit count]
        return self.kv[key][0].val

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: void
        """
        if self.cap == 0:
            return
        if key in self.kv:
            self.kv[key][0].val = value
            self.moveforward(key)
            return
        if len(self.kv) > self.cap:
            self.remove(self.tail.prev.key)
        self.add(key, value, 0)


    def remove(self, key):
        node, cnt = self.kv[key]
        if self.cnt[cnt] != node:
            node.prev.connect(node.next)
        elif self.kv[node.next.key][1] == cnt:
            node.prev.connect(node.next)
            self.cnt[cnt] = self.cnt[cnt].next
        else:
            node.prev.connect(node.next)
            del self.cnt[cnt]
        del self.kv[key]

    def add(self, key, value, cnt):
        if cnt in self.cnt:
            loc = self.cnt[cnt]
        else:
            # the list is in decresing order by cnt
            loc = self.cnt[cnt - 1]
        node = ListNode(key, value)
        loc.prev.connect(node)
        node.connect(loc)
        self.cnt[cnt] = node
        self.kv[key] = [node, cnt]
        


# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.set(key,value)
