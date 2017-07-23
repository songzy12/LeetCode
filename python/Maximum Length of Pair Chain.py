class Solution(object):
    
    def findLongestChain(self, pairs):
        """
        :type pairs: List[List[int]]
        :rtype: int
        """

        if not pairs:
            return 0
        
        pairs.sort(key=lambda x:x[-1])
        #print pairs
        count = 1
        cur = pairs[0][-1]
        for i in range(1, len(pairs)):
            if pairs[i][0] > cur:
                count += 1
                cur = pairs[i][1]
        return count
        

# https://stackoverflow.com/questions/17530303/longest-chain-of-pairs?rq=1
# greedy algorithm

pairs = [[7,9],[4,5],[7,9],[-7,-1],[0,10],[3,10],[3,6],[2,3]]
print Solution().findLongestChain(pairs)
