# https://leetcode.com/problems/race-car/description/
class Solution:

    def racecar(self, target):
        """
        :type target: int
        :rtype: int
        """
        visited = set([(0, 1)])
        pos = [(0, 1, 0)]
        while pos:
            cur_pos, cur_speed, cur_step = pos.pop(0)
            if cur_pos == target:
                return cur_step
            if cur_pos > 20000 or cur_pos < -20000:
                continue
            if (cur_pos + cur_speed, cur_speed * 2) not in visited:
                pos.append((cur_pos + cur_speed, cur_speed * 2, cur_step + 1))
                visited.add((cur_pos + cur_speed, cur_speed * 2))
            if (cur_pos, -1 if cur_speed > 0 else 1) not in visited:
                visited.add((cur_pos, -1 if cur_speed > 0 else 1))
                pos.append((cur_pos, -1 if cur_speed > 0 else 1, cur_step + 1))

target = 3
print(Solution().racecar(target))

# 嗯看着就像 dp

# 或者 BFS -> TLE
# 加一个剪枝