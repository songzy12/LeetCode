class Solution(object):
    def findErrorNums(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        m = {}
        a = None
        for num in nums:
            if num not in m:
                m[num] = True
            else:
                a = num
                # if you break here, then m is not completed
        b = None
        for i in range(1, len(nums)+1):
            if i not in m:
                b = i
                break
        return a, b
                
            
