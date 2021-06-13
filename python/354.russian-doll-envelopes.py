class Solution(object):
    def maxEnvelopes(self, envelopes):
        # http://www.geeksforgeeks.org/longest-monotonically-increasing-subsequence-size-n-log-n/
        end = [None] * len(envelopes)
        hi = 0
        import bisect
        for _, h in sorted(envelopes, key=lambda (w, h): (w, -h)):
            # hi is the length of current longest active list
            i = bisect.bisect_left(end, h, hi=hi)
            end[i] = h
            # i == hi means end is larger than any end element
            hi += i == hi
        return hi
        
        
envelopes = [[5,4],[6,4],[6,7],[2,3]]
print Solution().maxEnvelopes(envelopes)
