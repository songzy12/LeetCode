class Solution(object):
    def findMaxLength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        prefix = [0]
        for i, num in enumerate(nums):
            prefix.append(prefix[i] + (1 if num == 1 else -1))
        from collections import defaultdict
        m = defaultdict(list)
        for i, t in enumerate(prefix):
            m[t].append(i)
        ans = 0
        for t in m:
            ans = max(ans, m[t][-1] - m[t][0])
        return ans


if __name__ == '__main__':
    nums = [0,1]
    print Solution().findMaxLength(nums)

# brute force can work, but not elegant

# this is kind of partial sum
# see 0 as -1, 1 as 1, then we want the sum to be 0
# partial sum is the difference of two prefix sums
# if we put all the same prefix sums in a list
# then the longest one is between the last and the first
