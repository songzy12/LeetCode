# Equations are given in the format A / B = k,
# where A and B are variables represented as strings, and k is a real number (floating point number).
# Given some queries, return the answers. If the answer does not exist, return -1.0. 

class Solution(object):
    def calcEquation(self, equations, values, queries):
        """
        :type equations: List[List[str]]
        :type values: List[float]
        :type queries: List[List[str]]
        :rtype: List[float]
        """
        def seeker(a, b, path=[]):
            # seek the result of a/b
            if a not in dct.keys() or b not in dct.keys():      # No solution
                return 0
            if b in dct[a]:                       # This is it!
                return dct[a][b]
            else:                                 # Keep looking for solution
                tmp = []
                for c in dct[a].keys():
                    if c not in path and (seeker(c, b, path+[c])):
                        return dct[a][c]*(seeker(c, b, path+[c]))

        dct = {}                              # Put every number into the dict
        for i in xrange(len(equations)):
            nums = equations[i]
            div = float(values[i])
            if nums[0] in dct.keys():
                dct[nums[0]][nums[1]] = div
            else:
                dct[nums[0]] = {nums[0]:1, nums[1]:div}
            if nums[1] in dct.keys():
                dct[nums[1]][nums[0]] = 1.0/div
            else:
                dct[nums[1]] = {nums[1]:1, nums[0]:1.0/div}

        res = []
        for pair in queries:                    # seek the solution
            if seeker(pair[0], pair[1]):
                res += seeker(pair[0], pair[1]),
            else:
                res += -1,

        return [float(n) for n in res]
        
# first thought: graph, edges, search
# for pair a / b = k, both dict[a][b] = k, dict[b][a] = 1/k
# thus ensure the existence of solution in O(1)
