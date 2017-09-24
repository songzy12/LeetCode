class Solution(object):
    def judgePoint24(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if len(nums) == 1:
            return math.isclose(nums[0], 24)
        return any(self.judgePoint24([x] + rest)
                   for a, b, *rest in itertools.permutations(nums)
                   for x in {a+b, a-b, a*b, b and a/b})

# enumerate is possible
# but how to solve the division problem?
# you can store it as a / b, but it is complex

# it turns out there is a `math.isclose` in python

# also, there is a `itertools.permutations` in python

# `b and a/b` to deal with b == 0
