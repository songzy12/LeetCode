# Definition for a undirected graph node
class UndirectedGraphNode:
    def __init__(self, x):
        self.label = x
        self.neighbors = []

class Solution:
    # @param node, a undirected graph node
    # @return a undirected graph node
    def __init__(self):
        self.m = {} # map between old and new nodes, just like LRU
    def cloneGraph(self, node):
        if not node:
            return node
        if node not in self.m: # if in, neighbors all ready
            self.m[node] = UndirectedGraphNode(node.label)
            for x in node.neighbors:
                self.m[node].neighbors += [self.cloneGraph(x)]
        return self.m[node]

nodeA = UndirectedGraphNode('A')
nodeB = UndirectedGraphNode('B')
nodeD = UndirectedGraphNode('D')
nodeC = UndirectedGraphNode('C')
nodeA.neighbors = [nodeB, nodeD]
nodeB.neighbors = [nodeA, nodeC]
nodeC.neighbors = [nodeB, nodeD]
nodeD.neighbors = [nodeC, nodeA]
node = Solution().cloneGraph(nodeA)
print(node.label, [x.label for x in node.neighbors])
for t in node.neighbors:
    print(t.label, [x.label for x in t.neighbors])
