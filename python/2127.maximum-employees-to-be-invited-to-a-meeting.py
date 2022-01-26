# https://leetcode.com/problems/maximum-employees-to-be-invited-to-a-meeting

from collections import defaultdict


class Solution:
    # each node can appear in at most one cycle or a path points to a cycle.
    # the answer would be
    # 1. length of the largest cycle.
    # 2. lenght of all pair cycles + two longest path points to a pair cycle.
    def maximumInvitations(self, favorite):
        degree = {k: 0 for k in range(len(favorite))}
        for person in favorite:
            degree[person] += 1

        # the next circle id we would use
        circle_cnt = 0
        # map each node to the circle id it belongs to
        circle_id = {}
        # map each circle to its circle length
        circle_len = {}
        # map each circle to the length of the longest path connected
        circle_path_len_max = {}

        while len(degree):
            # find the head which has no parent
            # this would be used as the start of next path
            head = None
            cur_group = []

            for node in degree:
                if degree[node] == 0:
                    head = node
                    cur_group.append(head)

                    degree.pop(head)
                    degree[favorite[head]] -= 1
                    break
            if head == None:
                break

            # find the path / circlr starting from head
            visited = {head: True}
            while favorite[head] not in visited and \
                    favorite[head] not in circle_id:
                head = favorite[head]
                visited[head] = True
                cur_group.append(head)
                if degree[head] == 0:
                    degree.pop(head)
                    degree[favorite[head]] -= 1

            # favorite[head] is the connection point of path and circle
            if favorite[head] not in circle_id:
                # we found a new circle
                pos = cur_group.index(favorite[head])
                circle_len[circle_cnt] = len(cur_group) - pos
                circle_path_len_max[circle_cnt] = defaultdict(int)
                circle_path_len_max[circle_cnt][favorite[head]] = pos
                for node in cur_group[pos:]:
                    circle_id[node] = circle_cnt
                circle_cnt += 1
            else:
                # we found a known circle
                cur_circle_path = len(cur_group)
                cur_circle_id = circle_id[favorite[head]]
                circle_path_len_max[cur_circle_id][favorite[head]] = max(
                    cur_circle_path, circle_path_len_max[cur_circle_id][favorite[head]])

        # print(circle_cnt)
        # print(circle_len)
        # print(circle_path_len_max)

        # From now on, there is no node with in-degree 0.
        while len(degree):
            for head in degree.keys():
                break
            visited = {head: True}
            degree.pop(head)
            cur_group = [head]
            while favorite[head] not in visited:
                head = favorite[head]
                visited[head] = True
                degree.pop(head)
                cur_group.append(head)
            if favorite[head] not in circle_id:
                pos = cur_group.index(favorite[head])
                circle_len[circle_cnt] = len(cur_group) - pos
                circle_path_len_max[circle_cnt] = defaultdict(int)
                circle_path_len_max[circle_cnt][favorite[head]] = pos
                for node in cur_group[pos:]:
                    circle_id[node] = circle_cnt
                circle_cnt += 1

        # then let us compute the answer candidates
        # 1. sum of length of pair circles with arms
        # 2. the length of longest non-pair circles
        pair_circles_with_arms = 0
        longest_circle = 0
        for circle in range(circle_cnt):
            if circle_len[circle] == 2:
                pair_circles_with_arms += sum(
                    circle_path_len_max[circle].values()) + 2
            else:
                longest_circle = max(longest_circle,   circle_len[circle])

        # print(longest_circle, pair_circles_with_arms)
        return max(longest_circle, pair_circles_with_arms)


favorite = [1, 0, 0, 2, 1, 4, 7, 8, 9, 6, 7, 10, 8]
print(favorite)
assert Solution().maximumInvitations(favorite) == 6
print()

#          [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
favorite = [7, 0, 7, 13, 11, 6, 8, 5, 9, 8, 9, 14, 15, 7, 11, 6]
print(favorite)
assert Solution().maximumInvitations(favorite) == 11
