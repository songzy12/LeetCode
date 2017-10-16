class Solution(object):
    def canPartitionKSubsets(self, nums, k):
        target, rem = divmod(sum(nums), k)
        if rem or max(nums) > target: return False

        memo = [None] * (1 << len(nums))
        memo[-1] = True
        def search(used, todo):
            if memo[used] is None:
                targ = (todo - 1) % target + 1
                memo[used] = any(search(used | (1<<i), todo - num)
                                 for i, num in enumerate(nums)
                                 if (used >> i) & 1 == 0 and num <= targ)
            return memo[used]

        return search(0, target * k)

# this is also a typical problem
