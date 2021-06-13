# https://leetcode.com/contest/weekly-contest-240/problems/maximum-distance-between-a-pair-of-values/

class Solution:
    def maxDistance(self, nums1: List[int], nums2: List[int]) -> int:
        index_i = index_j = 0
        max_dis = 0
        while index_i < len(nums1):
            while index_j < len(nums2) and index_j < index_i:
                index_j += 1
            while index_j < len(nums2) and nums1[index_i] <= nums2[index_j]:
                index_j += 1
            if index_j < index_i or index_j == 0 or nums1[index_i] > nums2[index_j - 1]:
                index_i += 1
                continue
            max_dis = max(max_dis, index_j - 1 - index_i)
            index_i += 1
        return max_dis
