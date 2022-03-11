# https://leetcode.com/contest/weekly-contest-250/problems/maximum-genetic-difference-query/
#
# For fixed set of nodes and a value, we can build trie from the nodes and find the max value of xor between value in O(1).
# Now, given the constrain that the nodes can only be from the path up to root, we use dfs from root to enumerate the path.
# In each step of the dfs, we
# 1. insert the current node to trie;
# 2. check the query with the current node, compute the xor with target value.
# 3. remove the current node from trie.

from typing import List


class TrieNode:
    def __init__(self):
        self.child = {}
        self.go = 0  # Number of elements goes through this node

    def increase(self, number, d):
        cur = self
        for i in range(17, -1, -1):
            bit = (number >> i) & 1
            if bit not in cur.child:
                cur.child[bit] = TrieNode()
            cur = cur.child[bit]
            cur.go += d

    def findMax(self, number):
        cur, ans = self, 0
        for i in range(17, -1, -1):
            bit = (number >> i) & 1
            if (1-bit) in cur.child and cur.child[1-bit].go > 0:
                cur = cur.child[1 - bit]
                ans |= (1 << i)
            else:
                cur = cur.child[bit]
        return ans


class Solution:
    def maxGeneticDifference(self, parents: List[int], qs: List[List[int]]) -> List[int]:
        n, m, root = len(parents), len(qs), -1
        ans, trieNode = [-1] * m, TrieNode()
        graph, queryByNode = [[] for _ in range(n)], [[] for _ in range(n)]
        for i, p in enumerate(parents):
            if p == -1:
                root = i
            else:
                graph[p].append(i)

        for i, q in enumerate(qs):
            # node -> list of pairs (val, idx)
            queryByNode[q[0]].append((q[1], i))

        def dfs(u):
            trieNode.increase(u, 1)
            for val, idx in queryByNode[u]:
                ans[idx] = trieNode.findMax(val)
            for v in graph[u]:
                dfs(v)
            trieNode.increase(u, -1)

        dfs(root)
        return ans
