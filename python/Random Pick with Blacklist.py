# https://leetcode.com/problemset/algorithms/?difficulty=Hard&status=Todo
# https://leetcode.com/problems/random-pick-with-blacklist/description/
import random


class Solution:

    def __init__(self, N, blacklist):
        """
        :type N: int
        :type blacklist: List[int]
        """
        self.B = sorted(blacklist)
        self.N = N - len(blacklist)

    def pick(self):
        """
        :rtype: int
        """
        image = random.randint(0, self.N - 1)  # 0 to N-1
        if not self.B:  # NOTE: this
            return image
        # here we want to compute the preimage
        # we want to compute the cnt
        # if the index of insert image + k to B is k, then cnt = k
        # if the index of insert image + k to B is less than k, then cnt > k
        if image < self.B[0]:
            return image
        if image + len(self.B) > self.B[-1]:
            return image + len(self.B)

        def check(k):

            if self.B[k - 1] < image + k < self.B[k]:
                return 0
            if image + k >= self.B[k]:
                return -1
            return 1

        left = 0
        right = len(self.B)
        while left < right:
            k = (left + right) // 2
            temp = check(k)
            if temp == 0:
                return image + k  # image + k
            elif temp < 0:
                left = k
            else:
                right = k
        return -1

# Your Solution object will be instantiated and called as such:
N = 5
blacklist = [0, 1, 4]
obj = Solution(N, blacklist)
for t in range(10):
    print(obj.pick())

# 我只能想到 random 选，
# 然后如果落到了 black list 里面就重选

# 好吧所以我可以只调用一次 random
# 就计算一下可选的个数，然后 random 决定输出第几个
# 然后 binary search 决定一下那个应该是第几个
