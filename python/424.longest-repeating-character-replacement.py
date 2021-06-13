class Solution(object):
    def characterReplacement(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        def characterReplacement(self, s, k):
            res = lo = hi = 0
            counts = collections.Counter()
            for hi in range(1, len(s)+1):
                counts[s[hi-1]] += 1
                max_char_n = counts.most_common(1)[0][1]
                if hi - lo - max_char_n > k:
                    counts[s[lo]] -= 1
                    lo += 1
            return hi - lo
        
#The problem says that we can make at most k changes to the string (any character can be replaced with any other character). So, let's say there were no constraints like the k. Given a string convert it to a string with all same characters with minimal changes. The answer to this is
    #length of the entire string - number of times of the maximum occurring character in the string
#Given this, we can apply the at most k changes constraint and maintain a sliding window such that
    #(length of substring - number of times of the maximum occurring character in the substring) <= k
