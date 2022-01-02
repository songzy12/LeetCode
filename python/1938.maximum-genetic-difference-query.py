# https://leetcode.com/contest/weekly-contest-250/problems/maximum-genetic-difference-query/
#
# TLE

class Solution(object):
    def maxGeneticDifference(self, parents, queries):
        """
        :type parents: List[int]
        :type queries: List[List[int]]
        :rtype: List[int]
        """
        results = []
        for node, value in queries:
            result = node ^ value
            while parents[node] != -1:
                node = parents[node]
                result = max(result, node ^ value)
            results.append(result)
        return results
