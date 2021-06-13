class Node(object):
    def __init__(self, num):
        self.sum = num
        self.child = {}
    
class MapSum(object):
    
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = Node(0)
        self.value = {}

    def insert(self, key, val):
        """
        :type key: str
        :type val: int
        :rtype: void
        """
        pre = 0
        if key in self.value:
            pre = self.value[key]
        self.value[key] = val
        val -= pre
        
        cur = self.root
        for c in key:
            if c not in cur.child:
                cur.child[c] = Node(0)
            cur.child[c].sum += val
            cur  = cur.child[c]

    def sum(self, prefix):
        """
        :type prefix: str
        :rtype: int
        """
        cur = self.root
        for c in prefix:
            if c not in cur.child:
                return 0
            cur = cur.child[c]
        return cur.sum
            


# Your MapSum object will be instantiated and called as such:
# obj = MapSum()
# obj.insert(key,val)
# param_2 = obj.sum(prefix)
