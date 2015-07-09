class Solution:
    # @return a list of lists of length 3, [[val1,val2,val3]]
    def threeSum(self, num):
        result = []
        if num.count(0) >= 3:
            result += [[0,0,0]]
        pos = set()
        neg = set()
        dup = set()
        for i in num:
            if i > 0:
                if i not in pos:
                    pos.add(i)
                else:
                    dup.add(i)
            if i < 0:
                if i not in neg:
                    neg.add(i)
                else:
                    dup.add(i)
        pos = list(pos)
        neg = list(neg)
        pos.sort()
        neg.sort()
        for i in dup:
            if i < 0 and -2*i in pos:
                result += [[i, i, -2*i]]
            if i > 0 and -2*i in neg:
                result += [[-2*i, i, i]]
        if num.count(0) >= 1:
            for i in pos:
                if -i in neg:
                    result += [[-i, 0, i]]
        len_pos = len(pos)
        len_neg = len(neg)
        for i in range(len_pos-1):
            for j in range(i+1, len_pos):
                if -pos[i]-pos[j] in neg:
                    result += [[-pos[i]-pos[j], pos[i], pos[j]]]
        
        for i in range(len_neg-1):
            for j in range(i+1, len_neg):
                if -neg[i]-neg[j] in pos:
                    result += [[neg[i], neg[j], -neg[i]-neg[j]]]
        return result

#        result = []
#        i = 0                                    
#        while i < len(num):
#            time = num.count(num[i])
#            if time > 2 and num[i] == 0:
#                result += [[num[i], num[i], num[i]]]
#            if time > 1 and -2*num[i] in num[i+time:]:
#                result += [[num[i], num[i], -2*num[i]]]
#            temp = self.twoSum(num[i+time:], - num[i])
#            if temp:
#                result += [[num[i]] + j for j in temp]
#            i += time
#        return result
#    def twoSum(self, num, val):
#        result = []
#        i = 0
#        while i < len(num):
#            time = num.count(num[i])
#            if time > 1 and 2*num[i] == val:
#                result += [[num[i], num[i]]]
#            if val - num[i] in num[i+time:]:
#                result += [[num[i], val - num[i]]]
#            i += time
#        return result

import random   
S = [random.randint(-10,10) for i in range(10)]
S.sort()
print(S)
print(Solution().threeSum(S))
