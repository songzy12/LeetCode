class Solution:
    # @param num, a list of integer
    # @return an integer
    def rob(self, num):
        if len(num) == 0:
            return 0
        n1 = 0
        n2 = num[0]
        for i in range(1, len(num)):
            n1 = max(n2, n1+num[i])
            n1, n2 = n2, n1
        return n2
##        if len(num) == 1:
##            return num[0]
##        return max(num[0]+self.rob(num[2:]), self.rob(num[1:]))

num = [183,219,57,193,94,233,202,154,65,240,97,234,100,249,186,
       66,90,238,168,128,177,235,50,81,185,165,217,207,88,80,
       112,78,135,62,228,247,211]
print(Solution().rob(num))
        

