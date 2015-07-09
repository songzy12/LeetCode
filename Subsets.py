class Solution:
    # @param S, a list of integer
    # @return a list of lists of integer

    def subsets(self, S):
        l=[]
        if len(S)==0:
            return [[]]
        else:
            S.sort()
            S.reverse()
            t=self.subsets(S[1:])
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

S=[1,2]
print(Solution().subsets(S))

# S1=S[:]
# S2=list(S)
# import copy
# S3=copy.deepcopy(S)
# print(id(S),id(S1))
