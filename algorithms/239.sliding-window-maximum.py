class Solution:
    # @param {integer[]} nums
    # @param {integer} k
    # @return {integer[]}
    class Monoqueue:        
        def __init__(self):
            self.q = []
            
        def push(self, val):
            count = 0 
            while self.q and self.q[-1][0] < val:
                count += self.q[-1][1] + 1# how many values smaller ahead
                self.q.pop(-1)
            self.q.append([val, count])
            
        def pop(self):
            if self.q[0][1] > 0:
                self.q[0][1] -= 1
            else:
                self.q.pop(0)

        def maxi(self):
            return self.q[0][0]
            
            
    def maxSlidingWindow(self, nums, k):
        ans = []
        if not nums:
            return ans
        mq = self.Monoqueue()
        for i in range(k):
            mq.push(nums[i])
        for i in range(k, len(nums)):
            ans.append(mq.maxi())
            mq.pop()
            mq.push(nums[i])
        ans.append(mq.maxi())
        return ans

nums = [1,3,-1,-3,5,3,6,7]
k = 3
nums = []
k = 0
nums = [-6,-10,-7,-1,-9,9,-8,-4,10,-5,2,9,0,-7,7,4,-2,-10,8,7]
k = 7
print(Solution().maxSlidingWindow(nums, k))
