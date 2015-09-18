class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
##        ans=[]
##        candidates.sort()
##        for ii,elem in enumerate(candidates):
##            if target>elem:
##                subList=self.combinationSum2(candidates[ii+1:],target-elem)
##                if subList:
##                    ans+=[[elem]+lis for lis in subList if [elem]+lis not in ans]
##            elif target==elem:
##                if [elem] not in ans:
##                    ans+=[[elem]]
##            else:
##                break
##        return ans

##        # TLE
##        candidates.sort()
##        if target < 0:
##            return []
##        if not len(candidates):
##            return [[]] if not target else []
##        return self.combinationSum2(candidates[1:], target) + \
##               [[candidates[0]] + i for i in self.combinationSum2(candidates[1:], target-candidates[0])]
    
candidates = [23,29,8,24,5,7,25,29,18,18,32,29,30,5,9,23,27,15,28,32,11,24,11,29,12,32,5,7,31,16,7,19,10,33,8,10,5,21,26,18,26,23,5,21,24,31,31,8,11,16,5,17,5,33,34,12,31,26,7,27]
target = 22 
print Solution().combinationSum2(candidates, target)
