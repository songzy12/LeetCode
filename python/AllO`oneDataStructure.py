class Node(object):
    """
    double linked list node
    """
    def __init__(self,value=0,key_map = {}):
        self.value = value
        self.key_map = key_map  #{key:1}
        self.prev = None
        self.next = None
        
class AllOne(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.key_dict = {}     #{key:node(value,{key:1})}
        self.head = Node()     #to track min
        self.tail = self.head  #to track max
            
    def inc(self, key):
        """
        Inserts a new key <Key> with value 1. Or increments an existing key by 1.
        :type key: str
        :rtype: void
        """
        node = None
        if self.key_dict.has_key(key):
            node = self.key_dict[key]
            del node.key_map[key]
        else:
            node = self.head
            
        if node.next == None:
            node.next = Node(node.value+1,{key:1})
            node.next.prev = node
            self.tail = node.next
        elif node.next.value == node.value + 1:
            node.next.key_map[key] = 1
        else:
            next = Node(node.value+1,{key:1})
            node.next.prev = next
            next.next = node.next
            next.prev = node
            node.next = next
            
        self.key_dict[key] = node.next
        if len(node.key_map) == 0 and node.value > 0:
            node.next.prev = node.prev
            node.prev.next = node.next

    def dec(self, key):
        """
        Decrements an existing key by 1. If Key's value is 1, remove it from the data structure.
        :type key: str
        :rtype: void
        """
        if self.key_dict.has_key(key) is False:
            return
        
        node = self.key_dict[key]
        if node.value == 1:
            del self.key_dict[key]
        elif node.prev.value == node.value - 1:
            node.prev.key_map[key] = 1
            self.key_dict[key] = node.prev
        else:
            prev = Node(node.value - 1,{key:1})
            node.prev.next = prev
            prev.prev = node.prev
            prev.next = node
            node.prev = prev
            
            self.key_dict[key] = node.prev

        del node.key_map[key]
        if len(node.key_map) == 0:
            if node.next == None:
                node.prev.next = None
                self.tail = node.prev
            else:
                node.next.prev = node.prev
                node.prev.next = node.next


    def getMaxKey(self):
        """
        Returns one of the keys with maximal value.
        :rtype: str
        """
        if self.tail.value == 0:
            return ""
        return iter(self.tail.key_map).next()

        

    def getMinKey(self):
        """
        Returns one of the keys with Minimal value.
        :rtype: str
        """
        if self.head.next == None:
            return ""

        return iter(self.head.next.key_map).next()
