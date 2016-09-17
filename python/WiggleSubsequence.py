# A sequence of numbers is called a wiggle sequence if the differences between successive numbers strictly alternate between positive and negative.
# Given a sequence of integers, return the length of the longest subsequence that is a wiggle sequence.
# A subsequence is obtained by deleting some number of elements (eventually, also zero) from the original sequence, leaving the remaining elements in their original order.

class Solution(object):
    def wiggleMaxLength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        norep = [num for num, _ in itertools.groupby(nums)]
        if len(norep) < 2: return len(norep)
        triples = zip(norep, norep[1:], norep[2:])
        return 2 + sum(a<b>c or a>b<c for a, b, c in triples)    
        
# if we do this with all increasing or decreasing streaks,
# keep only their first and last number,
# then all the numbers we have left are local extrema,
# either smaller than both neighbors or larger than both neighbors.
# Which means that at that point, we're already fully wiggly.
# And we only removed as many numbers as we have to.
# So it's a longest possible wiggly subsequence.
