# https://leetcode.com/contest/weekly-contest-240/problems/maximum-subarray-min-product/
#
# Divide and Conquer?
# The min value would divide the array to be left and right.
# For the span contains the min value, the max subarray min-prod is simply min value * sum all.
# Then we compute the left and right ones recursively.
#
# Another way to think:
# With nums[i] as the min value, the candidate answer is nums[i] * sum(left_bound[i], right_bound[i]).
#   left_bound: index of the farthest element greater or equal to nums[i] in the left side.
#   right_bound: index of the farthest element greater or equal to nums[i] in the right side.
#
# The sum(left_bound, right_bound) can be computed by prefix sum.
# Here is how we compute left_bound:
# We maintain a mono increase stack, for each nums[i], we pop until we find the one less than nums[i], and then push nums[i].

from typing import List


def compute_left_bound(nums):
    left_bound = []
    stack = []
    for i, num in enumerate(nums):
        while stack:
            top = stack[-1]
            if top[-1] >= num:
                stack.pop()
            else:
                left_bound.append(top[0]+1)
                stack.append([i, num])
                break
        if not stack:
            stack.append([i, num])
            left_bound.append(0)
    return left_bound


def compute_right_bound(nums):
    left_bound = compute_left_bound(nums[::-1])

    right_bound = [0 for i in range(len(nums))]

    for i in range(len(nums)):
        right_bound[i] = len(nums) - 1 - left_bound[len(nums)-1-i]
    return right_bound


def compute_prefix_sum(nums):
    prefix_sum = [0]
    for num in nums:
        prefix_sum.append(prefix_sum[-1] + num)
    return prefix_sum


def compute_sum(prefix_sum, left, right):
    return prefix_sum[right + 1] - prefix_sum[left]


class Solution:
    def maxSumMinProduct(self, nums: List[int]) -> int:
        ans = 0

        left_bound = compute_left_bound(nums)
        right_bound = compute_right_bound(nums)
        prefix_sum = compute_prefix_sum(nums)

        for i in range(len(nums)):
            ans = max(ans, nums[i] * compute_sum(prefix_sum,
                                                 left_bound[i], right_bound[i]))
        return ans % (10**9+7)
