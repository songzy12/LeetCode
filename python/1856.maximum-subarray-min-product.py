# https://leetcode.com/contest/weekly-contest-240/problems/maximum-subarray-min-product/
# TLE

class Node:
    def __init__(self, val, index, left, right):
        self.val = val
        self.index = index

        self.left = left
        self.right = right

        self.sum = 0


def buildTree(nums, left, right):
    if left > right:
        return None

    min_val = 10**7+1
    index = -1
    for i in range(left, right+1):
        if nums[i] < min_val:
            min_val = nums[i]
            index = i

    node = Node(nums[index], index, buildTree(
        nums, left, index-1), buildTree(nums, index+1, right))
    node.sum = node.val + (node.left.sum if node.left else 0) + \
        (node.right.sum if node.right else 0)
    return node


def computeMinProd(node):
    if node == None:
        return 0
    return max(node.val * node.sum, computeMinProd(node.left), computeMinProd(node.right))


class Solution:
    def maxSumMinProduct(self, nums: List[int]) -> int:
        return computeMinProd(buildTree(nums, 0, len(nums)-1)) % (10**9+7)
