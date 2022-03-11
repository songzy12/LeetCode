# https://leetcode.com/problems/maximum-employees-to-be-invited-to-a-meeting

from collections import defaultdict


class Solution:
    def dfs1(self, node, r_favorite, visited):
        # run dfs from current node
        # check each of the nodes points to the curent node
        # find the longest path to this node
        depth = 1
        for v in r_favorite[node]:
            if v in visited:
                continue
            visited[v] = True
            depth = max(depth, 1+self.dfs1(v, r_favorite, visited))
        return depth

    def dfs2(self, node, favorite, visited):
        # starting from arbirary node, until we found a node that is already visited.
        if node in visited:
            return node, 0, False
        visited[node] = True
        visited_node, depth, cycle_detected = self.dfs2(
            favorite[node], favorite, visited)
        if visited_node == node:
            return visited_node, depth+1, True
        if cycle_detected:
            return visited_node, depth, True
        return visited_node, depth+1, False

    # each node can appear in at most one cycle or a path points to a cycle.
    # the answer would be the maximum of
    # 1. sum of length of pair circles with arms
    # 2. length of the largest cycle.

    def maximumInvitations(self, favorite):
        r_favorite = defaultdict(list)
        for u, v in enumerate(favorite):
            r_favorite[v].append(u)

        visited = {}

        # case 1
        # all the edges in the arms are pointing towards the pair nodes.
        # handling each pair nodes, we are handling n nodes and n edges.
        # for this case, we do not need to care about the favorite relationship.
        ans_1 = 0
        for u in range(len(favorite)):
            if u in visited:
                continue
            if favorite[favorite[u]] == u:
                visited[u] = True
                visited[favorite[u]] = True
                ans_1 += self.dfs1(u, r_favorite, visited)
                ans_1 += self.dfs1(favorite[u], r_favorite, visited)

        # case 2
        # for this case, we do not need to care about the reverse favorite relationship.
        ans_2 = 0
        for u in range(len(favorite)):
            if u in visited:
                continue
            visited_node, depth, cycle_detected = self.dfs2(
                u, favorite, visited)
            if cycle_detected:
                ans_2 = max(ans_2, depth)

        # the answer would be the max of case 1 and case 2
        return max(ans_1, ans_2)


favorite = [1, 0, 0, 2, 1, 4, 7, 8, 9, 6, 7, 10, 8]
print(favorite)
assert Solution().maximumInvitations(favorite) == 6
print()

#          [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
favorite = [7, 0, 7, 13, 11, 6, 8, 5, 9, 8, 9, 14, 15, 7, 11, 6]
print(favorite)
assert Solution().maximumInvitations(favorite) == 11
