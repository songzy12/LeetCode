class Solution:
    # @param num, a list of integer
    # @return a list of lists of integer
    def subsetsWithDup(self, S):
        l=self.auxSubsetsWithDup(S)
        # set() tuple()
        return [list(x) for x in set([tuple(x) for x in l])]
    def auxSubsetsWithDup(self, S):
        l=[]
        if len(S)==0:
            return [[]]
        else:
            S.sort()
            S.reverse()
            t=self.auxSubsetsWithDup(S[1:])
            # t is a list of lists
            l.extend(t)
            # be sure to use deepcopy
            # from copy import deepcopy
            # t1=deepcopy(t)
            t1=[x[:] for x in t]
            # S is a list of elements
            # x.append(S[0]) return None
            for x in t1:
                x.append(S[0])
            l.extend(t1)
            return l

S=[1,2,2]
print(Solution().subsetsWithDup(S))
##[[2],
## [1],
## [1,2,2],
## [2,2],
## [1,2],
## []]
