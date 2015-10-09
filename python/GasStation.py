class Solution:
    # @param gas, a list of integers
    # @param cost, a list of integers
    # @return an integer
    def canCompleteCircuit(self, gas, cost):
        # the idea is if you cannot go from i to j
        # then you can not go from any k\in[i,j] to j
        left=current=index=0
        # start from 0, and all is 0
        for i in range(len(gas)):
            # the gas left when at station i+1.
            left+=gas[i]-cost[i]
            current+=gas[i]-cost[i]
            if current<0:
                current=0
                index=i+1
                continue
        if left<0:
            return -1
        return index

##    def canCompleteCircuit(self, gas, cost):
##        for i in range(len(gas)):
##            gas[i]-=cost[i]
##        for i in range(len(gas)):
##            if self.isValid(gas, i):
##                return i
##        return -1
##
##    def isValid(self, gas, i):
##        sum=0
##        for x in gas[i:]+gas[:i]:
##            sum+=x
##            if sum<0:
##                return False
##        return True
        
print(Solution().canCompleteCircuit([0,1],[1,0]))
