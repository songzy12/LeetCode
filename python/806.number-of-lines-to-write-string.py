class Solution:
    def numberOfLines(self, widths, S):
        """
        :type widths: List[int]
        :type S: str
        :rtype: List[int]
        """
        S = map(lambda x: widths[ord(x)-ord('a')], S)
        # print(S)
        cnt = 0
        cur_length = 0
        for length in S:
            if cur_length + length <= 100:
                cur_length += length
            else:
                cnt += 1
                cur_length = length
        return [cnt+1, cur_length]

widths = [4,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10]
S = "a"
print(Solution().numberOfLines(widths, S))
