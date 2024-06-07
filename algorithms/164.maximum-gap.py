class Solution:
    # @param num, a list of integer
    # @return an integer
    def maximumGap(self, num):
        # num.sort()
        if len(num)<2:
            return 0
        
        for i in range(32): # bucket sort in linear time
            small=[]
            big=[]
            for n in num:
                if n>>i & 1 ==0:
                    small.append(n)
                else:
                    big.append(n)
            num=small+big

        gap=0
        for i in range(len(num)-1):
            temp=num[i+1]-num[i]
            if temp>gap:
                gap=temp
        return gap

import random
num=[random.randrange(2**32) for i in range(100)]
print(Solution().maximumGap(num))
