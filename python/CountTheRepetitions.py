# You are given two non-empty strings s1 and s2 (each at most 100 characters long) and 
# two integers 0 <= n1 <= 106 and 1 <= n2 <= 106. 
# Now consider the strings S1 and S2, where S1=[s1,n1] and S2=[s2,n2].
# Find the maximum integer M such that [S2,M] can be obtained from S1.

class Solution(object):
    def getMaxRepetitions(self, s1, n1, s2, n2):
        """
        :type s1: str
        :type n1: int
        :type s2: str
        :type n2: int
        :rtype: int
        """
        div = [0 for i in range(len(s2)+2)]
        mod = [0 for i in range(len(s2)+2)]
        p2 = 0
        c2 = 0
        i1 = i2 = -1
        for i in range(1, len(s2)+2):
            # compute div[i] and mod[i]
            for p1 in range(len(s1)):
                if s1[p1] != s2[p2]:
                    continue
                p2 += 1
                if p2 == len(s2):
                    c2 += 1
                    p2 = 0
            div[i] = c2
            mod[i] = p2
            for j in range(i):
                if mod[j] == mod[i]:
                    i1, i2 = j, i
                    break
            if i1 != -1:
                break
        # n1 may less than len(s2)
        if i1 == -1:
            return div[n1] / n2
        return ((div[i2]-div[i1])*((n1-i1)/(i2-i1)) + div[(n1-i1)%(i2-i1)+i1]) / n2
        
s1="nlhqgllunmelayl"
n1=2
s2="lnl"
n2=1
print Solution().getMaxRepetitions(s1, n1, s2, n2)

# no idea

# no need to care about n2 at first, 
# just divide the answer by n2 at last

# find what is (s1,i)/s2 and (s1,i)%s2 
# where (s1,i)%s2 is the next char of s2 after (s1,i)
# there would be a loop for i within s2.size()

# (s1,0)%s2 is not the same as (s1,s2.size())%s2
# since (s1,0)%s2 must be 0, 
# while (s1,s2.size()-1) may not cover s2 exactly

# suppose the loop is from i1 to i2-1: (s1,i1)%s2 == (s1,i2)%s2
# for each loop, the number of s2 is fixed within one loop 
# which is (s1,i2)/s2 - (s1,i1)/s2

# there are totally (n1-i1))/(i2-i1) loops
# before and after: (s1,(n1-i1)%(i2-i1)+i1)/s2
# note this is not the same as: (s1,i1)/s2 + (s1,(n1-i1)%(i2-i1))/s2


