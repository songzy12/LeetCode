# https://leetcode.com/contest/weekly-contest-240/problems/largest-color-value-in-a-directed-graph/

class Node:
    def __init__(self, index, color):
        self.index = index
        self.color = color
        self.child = []
        self.in_degree = 0
        self.up = {}


class Solution:
    def largestPathValue(self, colors: str, edges: List[List[int]]) -> int:
        nodes = []
        for i, color in enumerate(colors):
            nodes.append(Node(i, color))
        for i, j in edges:
            nodes[i].child.append(nodes[j])
            nodes[j].in_degree += 1

        roots = [node for node in nodes if node.in_degree == 0]

        res = 0
        while roots:
            root = roots.pop()
            up = root.up
            if root.color in up:
                up[root.color] += 1
            else:
                up[root.color] = 1

            if not root.child:
                for v in up.values():
                    res = max(res, v)

            for child in root.child:
                child.in_degree -= 1
                if child.in_degree == 0:
                    roots.append(child)
                for k, v in up.items():
                    if k in child.up:
                        child.up[k] = max(child.up[k], v)
                    else:
                        child.up[k] = v

        for node in nodes:
            if node.in_degree > 0:
                return -1
        return res
