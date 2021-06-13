# https://leetcode.com/contest/weekly-contest-64/problems/cracking-the-safe/

class Solution:
    def crackSafe(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        # length n, alphabet k
        # possible nodes: k^{n-1}, edges: k * k ^ {n-1} = k^n
        # each edge is a char, each node is a string
        # start from a string, then append a char each time

        
        
            
n = 1
k = 2
print(Solution().crackSafe(n, k))

# https://www.youtube.com/watch?v=iPLQgXUiU14
# https://www.geeksforgeeks.org/hierholzers-algorithm-directed-graph/
# https://en.wikipedia.org/wiki/De_Bruijn_sequence

# https://leetcode.com/problems/cracking-the-safe/discuss/113679/Very-simple-and-short-C++-solution-based-on-inverse-Burrows-Wheeler-transform
