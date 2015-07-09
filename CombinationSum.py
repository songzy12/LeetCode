class Solution:
    # @param candidates, a list of integers
    # @param target, integer
    # @return a list of lists of integers
    def combinationSum(self, candidates, target):
##        ans = []
##        candidates.sort()
##        # use sort once
##        for i, e in enumerate(candidates):
##            if e < target:
##                sub = self.combinationSum(candidates[i:], target - e)
##                
##                if sub:
##                    # the use of +=
##                    ans+=[[e]+e2 for e2 in sub]
##            elif e == target:
##                ans += [[e]]
##            else:
##                break
##        return ans
    
        if len(candidates)==0 or target==0:
            return []
        result=[]
        candidates.sort()
        if target % candidates[0]==0:
            result += [[candidates[0] for i in range(target//candidates[0])]]
        for i in range(target//candidates[0]+1):
            result0 = self.combinationSum(candidates[1:], target - i*candidates[0])
            if result0 != []:
                result1 = [candidates[0] for j in range(i)]
                if result1!=[]:
                    result0 = [ result1 + k for k in result0]
                result += result0
        return result
    
print(Solution().combinationSum([8, 7, 4, 3], 11))
# [[7], [2, 2, 3]]
